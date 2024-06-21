#!/usr/bin/python

# This document contains software used in the preparation of the
# article by:
#
# Davies S., Gait A., Rowley A., and Di Nuovo A.
# "Supervised Learning of Spatial Features with STDP and Homeostasis Using
# Spiking Neural Networks on SpiNNaker"
#
# The data and code are subject to the CC BY license, which can be found in the
# LICENSE.txt file within the same folder.
#
# If this software or data is used in derived publications, a citation to the
# mentioned article is appreciated by the authors.

import numpy as np
import pickle as pkl
import neo
import os
import re
import itertools
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mticker
from quantities import ms

# Function to compute the Hamming Distance between two numbers
def hamming_distance(x, y):
  return bin(x ^ y).count('1')

# Folder from which retrieve the data
folder = "Three patterns"
absolute_path = "./saved_data/"

# CSV file to which save the data
output_metrics_filename = "output_metrics_3.csv"
output_metrics_file = open(output_metrics_filename, 'w')

# Print column heading in the CSV file
column_title_string = "\"Code Word 0\", \"Code Word 1\", \"Code Word 2\", "
column_title_string += "\"HD0,1\", \"HD0,2\", \"HD(1,2)\", "
column_title_string += "\"Code Word Weight 0\", \"Code Word Weight 1\", \"Code Word Weight 2\", "
column_title_string += "\"Unit weight sum 0\", \"Unit weight sum 1\", "
column_title_string += "\"Weight sum 0\", \"Weight sum 1\", "
column_title_string += "\"Homeostasis factor\", "
column_title_string += "\"Positives\", "
column_title_string += "\"Negatives\", "
column_title_string += "\"True Positives\", "
column_title_string += "\"True Negatives\", "
column_title_string += "\"False Positives\", "
column_title_string += "\"False Negatives\", "
column_title_string += "\"Accuracy\", "
column_title_string += "\"Precision\", "
column_title_string += "\"Negative Prediction\", "
column_title_string += "\"Sensitivity\", "
column_title_string += "\"Specificity\"\n"
output_metrics_file.write(column_title_string)

# List of values for graphs
x_axis = list()
y_axis = list()
z_axis = list()
positives_list = list()
negatives_list = list()
true_positives_list = list()
true_negatives_list = list()
false_positives_list = list()
false_negatives_list = list()
accuracy_list = list()
precision_list = list()
negative_prediction_list = list()
sensitivity_list = list()
specificity_list = list()
homeostasis_factor_list = list()

# For each folder in the path indicated above
folder_path = os.path.join(absolute_path, folder)
for root, directories, files in os.walk(folder_path):
    for name in directories:
        experiment_folder = os.path.join(root,name)

        # Identify the pattern used with a regex from folder name
        x = re.findall(r'([0-9]*)\+([0-9]*)\+([0-9]*)', name)
        hd = list()
        hd.append(hamming_distance(int(x[0][0]), int(x[0][1])))
        hd.append(hamming_distance(int(x[0][0]), int(x[0][2])))
        hd.append(hamming_distance(int(x[0][1]), int(x[0][2])))

        # Open data files to extract spike information or present an error in case files are unavailable
        filename = "testing_output_spikes.pkl"
        testing_output_spikes_file_path = os.path.join(experiment_folder, filename)
        if os.path.isfile(testing_output_spikes_file_path) and os.path.exists(testing_output_spikes_file_path):
            a_file = open(testing_output_spikes_file_path, 'rb')
            testing_output_spikes = pkl.load(a_file)
            a_file.close()
        else:
            print ("Unable to use folder with patterns: {}".format(x))
            continue

        filename = "weight_exc_sum.pkl"
        weight_exc_sum_file_path = os.path.join(experiment_folder, filename)
        if os.path.isfile(weight_exc_sum_file_path) and os.path.exists(weight_exc_sum_file_path):
            a_file = open(weight_exc_sum_file_path, 'rb')
            weight_exc_sum = pkl.load(a_file)
            a_file.close()
        else:
            print ("Unable to use folder with patterns: {}".format(x))
            continue

        filename = "weight_inh_sum.pkl"
        weight_inh_sum_file_path = os.path.join(experiment_folder, filename)
        if os.path.isfile(weight_inh_sum_file_path) and os.path.exists(weight_inh_sum_file_path):
            a_file = open(weight_inh_sum_file_path, 'rb')
            weight_inh_sum = pkl.load(a_file)
            a_file.close()
        else:
            print ("Unable to use folder with patterns: {}".format(x))
            continue

        filename = "homeostasis_factor.pkl"
        homeostatis_file_path = os.path.join(experiment_folder, filename)
        if os.path.isfile(homeostatis_file_path) and os.path.exists(homeostatis_file_path):
            file_handle = open(homeostatis_file_path, 'rb')
            homeostasis_factor = pkl.load(file_handle)
            file_handle.close()
            print ("Filename: {}. Homeostasis factor: {}".format(homeostatis_file_path, homeostasis_factor))
        else:
            print ("Unable to use folder with patterns: {}".format(x))
            continue

        filename = "testing_output_spikes.pkl"
        spikes_file_path = os.path.join(experiment_folder, filename)
        if os.path.isfile(spikes_file_path) and os.path.exists(spikes_file_path):
            file_handle = open(spikes_file_path, 'rb')
            testing_output_spikes = pkl.load(file_handle)
            file_handle.close()
            testing_output_spikes = testing_output_spikes[0:1024]
        else:
            print ("Unable to use folder with patterns: {}".format(x))
            continue

        unit_factor = (weight_exc_sum+weight_inh_sum)[0] / 3

        weight_exc_float_unit = (weight_exc_sum / unit_factor)
        weight_inh_float_unit = (weight_inh_sum / unit_factor)
        weight_exc_units = [int(x) for x in weight_exc_float_unit]
        weight_inh_units = [int(x) for x in weight_inh_float_unit]

        final_weight_string = []
        for pattern_string in x[0]:
            bin_string = list(itertools.chain.from_iterable(bin(int(pattern_string))[2:].zfill(10)))
            final_weight = 0
            for index in range(len(bin_string)):
                if (bin_string[index] == '0'):
                    final_weight += weight_inh_units[index] - weight_exc_units[index]
                else:
                    final_weight += weight_exc_units[index] - weight_inh_units[index]
            final_weight_string.append(final_weight)

        # Retrieve statistics from data files
        user_list = list()
        user_list.append(int(x[0][0]))
        if int(x[0][1]) not in user_list:
            user_list.append(int(x[0][1]))
        if int(x[0][2]) not in user_list:
            user_list.append(int(x[0][2]))

        spike_count = 0
        positives = 0
        negatives = 0
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        for pattern in range(len(testing_output_spikes)):
            if testing_output_spikes[pattern]:
                positives += 1
                if pattern in user_list:
                    true_positive += 1
                else:
                    false_positive += 1
            else:
                negatives += 1
                if pattern in user_list:
                    false_negative += 1
                else:
                    true_negative += 1

        positives = true_positive + false_positive
        negatives = true_negative + false_negative

        # Compute metrics
        accuracy = (true_positive + true_negative)/(len(testing_output_spikes))
        precision = true_positive / (true_positive + false_positive)
        negative_prediction = true_negative / (true_negative + false_negative)
        sensitivity = true_positive / (true_positive + false_negative)
        specificty = true_negative / (true_negative + false_positive)

        # Prepare data for graphs
        if hd[0] != 0 and hd[1] != 0 and hd[2] != 0:
            x_axis.append(hd[0])
            y_axis.append(hd[1])
            z_axis.append(hd[2])
            positives_list.append(positives)
            negatives_list.append(negatives)
            true_positives_list.append(true_positive)
            true_negatives_list.append(true_negative)
            false_positives_list.append(false_positive)
            false_negatives_list.append(false_negative)
            accuracy_list.append(accuracy)
            precision_list.append(precision)
            negative_prediction_list.append(round(negative_prediction, 3))
            sensitivity_list.append(sensitivity)
            specificity_list.append(specificty)
            homeostasis_factor_list.append(homeostasis_factor)

        # output metrics in CSV file
        output_string = "{},{},{}".format(x[0][0], x[0][1], x[0][2])
        output_string += ",{},{},{}".format(hd[0], hd[1], hd[2])
        output_string += ",{},{},{}".format(final_weight_string[0], final_weight_string[1], final_weight_string[2])
        output_string += ",\"{}\",\"{}\"".format(weight_inh_units, weight_exc_units)
        output_string += ",\"{}\",\"{}\"".format(weight_inh_sum, weight_exc_sum)
        output_string += ",{}".format(homeostasis_factor)
        output_string += ",{}".format(positives)
        output_string += ",{}".format(negatives)
        output_string += ",{}".format(true_positive)
        output_string += ",{}".format(true_negative)
        output_string += ",{}".format(false_positive)
        output_string += ",{}".format(false_negative)
        output_string += ",{}".format(accuracy)
        output_string += ",{}".format(precision)
        output_string += ",{}".format(negative_prediction)
        output_string += ",{}".format(sensitivity)
        output_string += ",{}".format(specificty)
        output_string += "\n"

        output_metrics_file.write(output_string)

# Close CSV file
output_metrics_file.close()

# Create a 3D scatter plot with color mapping, one plot for each metric

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=positives_list, cmap='winter_r')
fig.colorbar(scatter, label='Positive identifications', location='left')
plt.title('Positive identifications')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=false_negatives_list, cmap='winter_r')
fig.colorbar(scatter, label='False Negatives', location='left', format=mticker.FixedFormatter(["2", "1", "0"]), ticks=[2, 1, 0])
plt.title('False Negatives')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=homeostasis_factor_list, cmap='winter_r')
fig.colorbar(scatter, label='Homeostatic factor', location='left')
plt.title('Homeostatic factor')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=accuracy_list, cmap='winter_r')
fig.colorbar(scatter, label='Accuracy', location='left')
plt.title('Accuracy')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=precision_list, cmap='winter_r')
fig.colorbar(scatter, label='Precision', location='left')
plt.title('Precision')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=negative_prediction_list, cmap='winter_r')
#fig.colorbar(scatter, label='Negative Prediction', location='left', format="$%1.3g$", ticks=[1.0, 0.999, 0.998], values=[1.0, 0.999, 0.998])
fig.colorbar(scatter, label='Negative Prediction', location='left', format=mticker.FixedFormatter(["1.0", "0.999", "0.998"]), ticks=[1.0, 0.999, 0.998])
plt.title('Negative Prediction')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=sensitivity_list, cmap='winter_r')
fig.colorbar(scatter, label='Sensitivity', location='left')
plt.title('Sensitivity')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=specificity_list, cmap='winter_r')
fig.colorbar(scatter, label='Specificity', location='left')
plt.title('Specificity')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x_axis, y_axis, z_axis, c=true_negatives_list, cmap='winter_r')
fig.colorbar(scatter, label='True negatives', location='left')
plt.title('True negatives')

ax.set_xlabel('HD(1,2)')
ax.set_ylabel('HD(1,3)')
ax.set_zlabel('HD(2,3)')
plt.show()
