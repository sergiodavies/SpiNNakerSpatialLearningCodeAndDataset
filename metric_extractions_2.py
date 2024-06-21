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
from quantities import ms

# Function to compute the Hamming Distance between two numbers
def hamming_distance(x, y):
  return bin(x ^ y).count('1')

# Folder from which retrieve the data
folder = "Two patterns"
absolute_path = "./saved_data/"

# CSV file to which save the data
output_metrics_filename = "output_metrics_2.csv"
output_metrics_file = open(output_metrics_filename, 'w')

# Print column heading in the CSV file
output_string = 'Code Word 0, Code Word 1, "HD0,1", Homeostasis factor, Positives, Negatives, True Positives, True Negatives, False Positives, False Negatives, Accuracy, Precision, Negative Prediction, Sensitivity, Specificity\n'
output_metrics_file.write(output_string)

# For each folder in the path indicated above
folder_path = os.path.join(absolute_path, folder)
for root, directories, files in os.walk(folder_path):
    for name in directories:
        experiment_folder = os.path.join(root,name)

        # Identify the pattern used with a regex from folder name
        x = re.findall(r'([0-9]*)\+([0-9]*)', name)
        hd = list()
        print (x)
        hd.append(hamming_distance(int(x[0][0]), int(x[0][1])))

        # Open data files to extract spike information or present an error in case files are unavailable
        filename = "homeostasis_factor.pkl"
        homeostatis_file_path = os.path.join(experiment_folder, filename)
        if os.path.isfile(homeostatis_file_path) and os.path.exists(homeostatis_file_path):
            file_handle = open(homeostatis_file_path, 'rb')
            homeostasis_factor = pkl.load(file_handle)
            file_handle.close()

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

        # Retrieve statistics from data files
        user_list = list()
        user_list.append(int(x[0][0]))
        if int(x[0][1]) not in user_list:
            user_list.append(int(x[0][1]))

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
        if (len(testing_output_spikes) == 0):
            accuracy = 0
        else:
            accuracy = (true_positive + true_negative)/(len(testing_output_spikes))

        if (positives == 0):
            precision = 0
        else:
            precision = true_positive / (true_positive + false_positive)

        if ((true_negative + false_negative) == 0):
            negative_prediction = 0
        else:
            negative_prediction = true_negative / (true_negative + false_negative)

        if ((true_positive + false_negative) == 0):
            sensitivity = 0
        else:
            sensitivity = true_positive / (true_positive + false_negative)

        if ((true_negative + false_positive) == 0):
            specificty = 0
        else:
            specificty = true_negative / (true_negative + false_positive)

        # output metrics in CSV file
        output_string = "{},{}".format(x[0][0], x[0][1])
        output_string += ",{}".format(hd[0])
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
