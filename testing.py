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

os.environ['C_LOGS_DICT'] = './logs/'  # Logging folder path
timestep = 1  # Simulation timestep in ms
spike_current = 20  # Synaptic weight required to produce a post-synaptic spike for each pre-synaptic spike received

number_of_bits = 10  # Number of bits in each code word
input_population_size = number_of_bits  # Each input population has one neuron per bit

spike_present_injection_time = [10]  # Time of the spike when an input neuron needs to fire
spike_not_present_injection_time = [100]  # Time of the spike when an input neuron does not need to fire. The simulation only lasts 20 ms, therefore the neuron never fires
# On the basis of these spike times, the output neuron can fire at most once per simulation

runtime = spike_present_injection_time[-1] + 10  # Simulation run time

#code word interval to test
start_bit_pattern = 0
end_bit_pattern = 2**number_of_bits


list_pattern = []  # list of input patterns
# List of number of output spikes for the corresponding pattern.
# Because of the way the network is constructed, this value can be either 0 or 1
output_spikes = []

# Folder where all the data being processed is stored
folder_list = ["./saved_data/"]

# This loop goes through all the folders in the list
# TODO: Probably this for loop is meaningless. However, leaving it here as this is the code used for the publication
for folder in folder_list:

    # Read the synaptic weights computer earlier in the process
    filename = "{}/homeostatic_weights_1.pkl".format(folder)
    a_file = open(filename, 'rb')
    weights_1 = pkl.load(a_file)
    a_file.close()

    filename = "{}/homeostatic_weights_0.pkl".format(folder)
    a_file = open(filename, 'rb')
    weights_0 = pkl.load(a_file)
    a_file.close()

    # Prepare a list of synaptic connections between neurons
    # Each connection requires four information (as described in FromListConnector in PyNN):
    # Source neuron, Destination Neuron, Weight and Delay
    list_connector_1 = []
    list_connector_0 = []

    for weight_index in range(len(weights_1)):
        if weights_1[weight_index] != 0:
            list_connector_1.append([weight_index, 0, weights_1[weight_index], 1])

        if weights_0[weight_index] != 0:
            list_connector_0.append([weight_index, 0, weights_0[weight_index], 1])

    # Create 25 identical networks and set different inputs for each of them.
    # Each network received as input a different code word
    # NOTE: As the simulation should test 1024 patters in batch of 25 patterns at a time
    # NOTE: There is an excess of 1 network that is simulated at the end with pattern 1024.
    # NOTE: As the number 1024 requires an additional bit which is not provided in the network structure,
    # NOTE: the last network is simulated with the code word "0" (which is also the first code word tested).
    # NOTE: The simulation is performed with 25 networks, and the output is saved in the file
    # NOTE: However, the last element of the list of outputs is discarded when the information is fetched
    # NOTE: to compute the metrics
    for bit_pattern_range in range (start_bit_pattern, end_bit_pattern, 25):

        print ("")
        print ("**************************")
        print ("**************************")
        print ("Folder {}".format(folder))
        print ("Calculating output for pattern {}-{}".format(bit_pattern_range, bit_pattern_range+24))
        print ("**************************")
        print ("**************************")
        print ("")

        # At every iteration of the simulation, the system requires setup
        # Therefore at every iteration the neuron type and the connections are set
        sim.setup(timestep=timestep)
        sim.set_number_of_neurons_per_core(sim.IF_curr_delta, 100)

        IF_curr_delta_model = sim.IF_curr_delta()

        output_neuron_list = []

        # Create each of the 25 instances of the network
        for bit_pattern in range(bit_pattern_range, bit_pattern_range+25):

            print ("")
            print ("**************************")
            print ("**************************")
            print ("Folder {}".format(folder))
            print ("Setting network for pattern {}".format(bit_pattern))
            print ("**************************")
            print ("**************************")
            print ("")

            spike_times_0 = []
            spike_times_1 = []
            bit_pattern_string = []

            for i in range(number_of_bits - 1, -1, -1):
                if (bit_pattern & (1 << i) == 0):
                    spike_times_0.append(spike_present_injection_time)
                    spike_times_1.append(spike_not_present_injection_time)
                    bit_pattern_string.append('0')
                else:
                    spike_times_0.append(spike_not_present_injection_time)
                    spike_times_1.append(spike_present_injection_time)
                    bit_pattern_string.append('1')

            list_pattern.append(bit_pattern_string)

            ssp_1 = sim.Population(input_population_size, sim.SpikeSourceArray(spike_times_1), label='ssp_1')
            ssp_0 = sim.Population(input_population_size, sim.SpikeSourceArray(spike_times_0), label='ssp_0')

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

            output_neuron.record(['spikes'])  # Record the output spikes

            output_neuron_list.append(output_neuron)

        print ("")
        print ("**************************")
        print ("**************************")
        print ("Folder {}".format(folder))
        print ("Starting simulation for pattern {}-{}".format(bit_pattern_range, bit_pattern_range+24))
        print ("**************************")
        print ("**************************")
        print ("")

        sim.run(runtime)  # Run the simulation with 25 networks

        # At the end of the simulation retrueve the output spikes from the output neuron of each of the network instances
        # And count if there have been any output spikes
        for single_output_neuron in output_neuron_list:
            spikesm = single_output_neuron.get_data().segments[0].spiketrains[0]

            output_spikes.append(len(spikesm))

            print ("Output spikes: {}".format(spikesm))

        # Terminate the simulation and reset the system for the next iteration
        sim.end()

    # Save the information related to the input patterns and the output spikes
    # is saved for future processing to extract the metrics
    filename = "{}/testing_bit_patterns.pkl".format(folder)
    v_file = open(filename, 'wb')
    pkl.dump(list_pattern, v_file)
    v_file.close()

    filename = "{}/testing_output_spikes.pkl".format(folder)
    v_file = open(filename, 'wb')
    pkl.dump(output_spikes, v_file)
    v_file.close()
