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

import spynnaker.pyNN as sim
import numpy as np
import pickle as pkl
import neo
import os
from quantities import ms
import decimal
import sys

os.environ['C_LOGS_DICT'] = './logs/'  # Logging folder path
timestep = 1  # Simulation timestep in ms
spike_current = 20  # Synaptic weight required to produce a post-synaptic spike for each pre-synaptic spike received

number_of_bits = 10  # Number of bits in each code word
input_population_size = number_of_bits  # Each input population has one neuron per bit

print ("Enter patterns separated by space:\n")  # User prompt to enter patterns against which to estimate homeostasis factor
bit_pattern = input()

spike_times = [10]  # Time of the spike when an input neuron needs to fire
no_spike_times = [100]  # Time of the spike when an input neuron does not need to fire. The simulation only lasts 20 ms, therefore the neuron never fires

runtime = 20  # Simulation run time

# Read the synaptic weights (excitatory and inhibitory) from file
filename = "saved_data/weight_exc_sum.pkl"
a_file = open(filename, 'rb')
weights_exc = pkl.load(a_file)
a_file.close()

filename = "saved_data/weight_inh_sum.pkl"
a_file = open(filename, 'rb')
weights_inh = pkl.load(a_file)
a_file.close()


# Function that iteratively runs the network given an homeostatic factor and the input spike times.
# The output of this funciton is the number of spikes emitted by the network
def run_network(homeostatis_factor, spike_times_0_array, spike_times_1_array):
    reduced_1_weights = homeostatis_factor * weights_exc
    reduced_0_weights = homeostatis_factor * weights_inh

    list_connector_1 = []
    list_connector_0 = []

    for weight_index in range(len(reduced_1_weights)):
        if reduced_1_weights[weight_index] != 0:
            list_connector_1.append([weight_index, 0, reduced_1_weights[weight_index], 1])

        if reduced_0_weights[weight_index] != 0:
            list_connector_0.append([weight_index, 0, reduced_0_weights[weight_index], 1])

    sim.setup(timestep=timestep)
    sim.set_number_of_neurons_per_core(sim.IF_curr_delta, 100)

    IF_curr_delta_model = sim.IF_curr_delta()

    ssp_1 = sim.Population(input_population_size, sim.SpikeSourceArray(spike_times_1_array), label='ssp_1')
    ssp_0 = sim.Population(input_population_size, sim.SpikeSourceArray(spike_times_0_array), label='ssp_0')

    injector_neurons_1 = sim.Population(input_population_size, IF_curr_delta_model, label='injector_neurons_1')
    injector_neurons_0 = sim.Population(input_population_size, IF_curr_delta_model, label='injector_neurons_0')

    output_neuron = sim.Population(1, IF_curr_delta_model, label='output_neuron')

    static_synapse = sim.StaticSynapse(weight=spike_current, delay=1)

    source_proj_1 = sim.Projection(ssp_1, injector_neurons_1, sim.OneToOneConnector(), static_synapse, receptor_type='excitatory')
    source_proj_0 = sim.Projection(ssp_0, injector_neurons_0, sim.OneToOneConnector(), static_synapse, receptor_type='excitatory')

    injector_proj_1_exc = sim.Projection(injector_neurons_1, output_neuron, sim.FromListConnector(list_connector_1), receptor_type='excitatory')
    injector_proj_1_inh = sim.Projection(injector_neurons_1, output_neuron, sim.FromListConnector(list_connector_0), receptor_type='inhibitory')
    injector_proj_0_exc = sim.Projection(injector_neurons_0, output_neuron, sim.FromListConnector(list_connector_0), receptor_type='excitatory')
    injector_proj_0_inh = sim.Projection(injector_neurons_0, output_neuron, sim.FromListConnector(list_connector_1), receptor_type='inhibitory')

    output_neuron.record(['spikes'])

    sim.run(runtime)

    spikesm = output_neuron.get_data().segments[0].spiketrains[0]

    sim.end()

    print (spikesm)

    spike_count = len(spikesm)

    return spike_count


# Function that iteratively tests various homeostatic factors on the neural network.
# The algorithm searches for the lowest value that allows the network to spike.
# The search is performed initially with a binary search in the interval 0.0001 - 100.
# If in this interval there is no spike generated, then the interval is expanded to 0.0001 - 1000.
# If the output neuron does not generate a spike, then an error is returned.
# Otherwise the interval narrows down with a binary search algorithm in first instance, then with a linear search.
def retrieve_factor(pattern):
    homeostatic_rate = 0.0001
    homeostatic_factor_start = homeostatic_rate
    homeostatic_factor_stop = 100
    homeostatis_factor = homeostatic_factor_stop
    no_homeostasis = False

    #generate spike times 1
    spike_times_1_array = []

    #generate spike times 0
    spike_times_0_array = []

    for bit_index in range(number_of_bits):
        if 1 << (9 - bit_index) & int(pattern) == 0:
            spike_times_0_array.append(spike_times)
            spike_times_1_array.append(no_spike_times)
        else:
            spike_times_0_array.append(no_spike_times)
            spike_times_1_array.append(spike_times)

    while (True):
        print ("")
        print ("**************************")
        print ("**************************")
        print ("Calculating weight homeostasis - pattern {} - exponential max search".format(pattern))
        print ("Attempting {}".format(homeostatis_factor))
        print ("**************************")
        print ("**************************")
        print ("")

        spike_count = run_network(homeostatis_factor, spike_times_0_array, spike_times_1_array)

        if spike_count >= 1:
            print ("Spikes obtained with homeostatis factor {}". format(homeostatis_factor))
            print ("Spike count: {}". format(spike_count))
            break

        else:
            homeostatis_factor *= 10

        if homeostatis_factor >= 1000:
            return None


    homeostatic_rate = 0.0001
    homeostatic_factor_start = homeostatic_rate
    homeostatic_factor_stop = homeostatis_factor
    homeostatis_factor = (homeostatic_factor_stop + homeostatic_factor_start) / 2

    while (True):

        print ("")
        print ("**************************")
        print ("**************************")
        print ("Calculating weight homeostasis - pattern {} - binary search".format(pattern))
        print ("Homeostatis start interval {}".format(homeostatic_factor_start))
        print ("Homeostatis stop interval {}".format(homeostatic_factor_stop))
        print ("Attempting {}".format(homeostatis_factor))
        print ("**************************")
        print ("**************************")
        print ("")

        spike_count = run_network(homeostatis_factor, spike_times_0_array, spike_times_1_array)

        if spike_count == 1:
            print ("Spikes obtained with homeostatis factor {}". format(homeostatis_factor))
            print ("Spike count: {}". format(spike_count))

        if (homeostatic_factor_stop - homeostatic_factor_start) > homeostatic_rate:
            if spike_count > 0:
                #homeostatic_factor_start = homeostatic_factor_start
                homeostatic_factor_stop = homeostatis_factor
            else:  # spike_count = 0
                #homeostatic_factor_stop = homeostatic_factor_stop
                homeostatic_factor_start = homeostatis_factor

            homeostatis_factor = (homeostatic_factor_stop + homeostatic_factor_start) / 2
        else:
            break


    homeostatic_rate = homeostatic_rate / 10.0
    d = decimal.Decimal(str(homeostatic_rate))
    homeostatic_decimal_places = abs(d.as_tuple().exponent)
    homeostatic_factor_start = round(homeostatic_factor_start, homeostatic_decimal_places) - 10**(-homeostatic_decimal_places)
    homeostatic_factor_stop  = round(homeostatic_factor_stop, homeostatic_decimal_places) + 10**(-homeostatic_decimal_places)

    for homeostatis_factor in np.arange(homeostatic_factor_start, homeostatic_factor_stop + homeostatic_rate, homeostatic_rate):

        print ("")
        print ("**************************")
        print ("**************************")
        print ("Calculating weight homeostasis - pattern {} - linear search.".format(pattern))
        print ("Homeostatis start interval {}".format(homeostatic_factor_start))
        print ("Homeostatis stop interval {}".format(homeostatic_factor_stop))
        print ("Attempting {}".format(homeostatis_factor))
        print ("**************************")
        print ("**************************")
        print ("")

        spike_count = run_network(homeostatis_factor, spike_times_0_array, spike_times_1_array)

        if spike_count == 1:
            print ("Spikes obtained with homeostatis factor {}". format(homeostatis_factor))
            print ("Spike count: {}". format(spike_count))
            return homeostatis_factor


# Generate pattern list against which to test the network
pattern_user_list_string = bit_pattern.split()
pattern_user_list = list()

for i in range(len(pattern_user_list_string)):
    if int(pattern_user_list_string[i]) not in pattern_user_list:
        pattern_user_list.append(int(pattern_user_list_string[i]))

# Trigger the simulation to retrieve the homeostasis factor for each specific pattern
pattern_factor_list = list()
homeostatis_factor_list = list()
for pattern in pattern_user_list:
    homeostasis_factor = retrieve_factor(pattern)
    # If a Homeostatic factor is found, insert it in the appropriate list
    if homeostasis_factor is not None:
        homeostatis_factor_list.append(homeostasis_factor)
        pattern_factor_list.append(pattern)

# Test that at least one homeostatic factor has been found
if len(homeostatis_factor_list) != 0:
    # Choose the maximum of the homeostatic factors retrieved
    homeostatis_factor = max(homeostatis_factor_list)

    reduced_1_weights = homeostatis_factor * weights_exc
    reduced_0_weights = homeostatis_factor * weights_inh

    print ("Minimum homeostatic factor: {}".format(homeostatis_factor))
    print ("Weights:")
    print (reduced_1_weights)
    print (reduced_0_weights)

    # Save all the data generated so far
    filename = "saved_data/pattern_factor_list.pkl"
    pattern_factor_list_file = open(filename, 'wb')
    pkl.dump(pattern_factor_list, pattern_factor_list_file)
    pattern_factor_list_file.close()

    filename = "saved_data/homeostatis_factor_list.pkl"
    homeostatis_factor_list_file = open(filename, 'wb')
    pkl.dump(homeostatis_factor_list, homeostatis_factor_list_file)
    homeostatis_factor_list_file.close()

    filename = "saved_data/homeostasis_factor.pkl"
    homeostatis_factor_file = open(filename, 'wb')
    pkl.dump(homeostatis_factor, homeostatis_factor_file)
    homeostatis_factor_file.close()

    filename = "saved_data/homeostatic_weights_1.pkl"
    exc_weights_file = open(filename, 'wb')
    pkl.dump(reduced_1_weights, exc_weights_file)
    exc_weights_file.close()

    filename = "saved_data/homeostatic_weights_0.pkl"
    inh_weights_file = open(filename, 'wb')
    pkl.dump(reduced_0_weights, inh_weights_file)
    inh_weights_file.close()
else:
    # Otherwise generate an error to say that homeostatic factors have not been found
    print ("No homeostatic factor found for patterns {}".format(pattern_user_list))
    sys.exit("Terminating")

