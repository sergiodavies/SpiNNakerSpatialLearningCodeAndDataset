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
import csv
import os
from quantities import ms

# Determine population size by opening one synaptic weight file.
# Excitatory synaptic weight file is the most likely to exist, and therefore the one used.
filename = "saved_data/weight_exc_final_packet0.pkl"
if os.path.isfile(filename):
    a_file = open(filename, 'rb')
    weights_exc = pkl.load(a_file)
    a_file.close()
else:
    print ("No weight file detected. Terminating")

# Read the number of weights in the file
input_population_size = len(weights_exc[-1].magnitude)

#generate two arrays for excitatory and inhibitory weights of the appropriate size
final_weights_exc = np.zeros(input_population_size)
final_weights_inh = np.zeros(input_population_size)

#Loop through all the synaptic weight files and add them on the appropriate array
i = 0
while(True):
    print ("Summing weights for pattern ID {}".format(i))

    filename = "saved_data/weight_exc_final_packet{}.pkl".format(i)
    if os.path.isfile(filename):
        a_file = open(filename, 'rb')
        weights_exc = pkl.load(a_file)
        a_file.close()
    else:
        break

    filename = "saved_data/weight_inh_final_packet{}.pkl".format(i)
    if os.path.isfile(filename):
        a_file = open(filename, 'rb')
        weights_inh = pkl.load(a_file)
        a_file.close()
    else:
        break

    final_weights_exc += weights_exc[-1].magnitude
    final_weights_inh += weights_inh[-1].magnitude

    i += 1

# Save the final excitatory and inhibitory weights
filename = "saved_data/weight_exc_sum.pkl"
exc_weights_file = open(filename, 'wb')
pkl.dump(final_weights_exc, exc_weights_file)
exc_weights_file.close()

filename = "saved_data/weight_inh_sum.pkl"
inh_weights_file = open(filename, 'wb')
pkl.dump(final_weights_inh, inh_weights_file)
inh_weights_file.close()
