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

class WeightRecorder(object):
    """
    Recording of weights is not yet built in to PyNN, so therefore we need
    to construct a callback object, which reads the current weights from
    the projection at regular intervals.
    """

    def __init__(self, sampling_interval, projection):
        self.interval = sampling_interval
        self.projection = projection
        self._weights = []

    def __call__(self, t):
        self._weights.append(self.projection.get('weight', format='list', with_address=False))
        return t + self.interval

    def get_weights(self):
        signal = neo.AnalogSignal(self._weights, units='nA', sampling_period=self.interval * ms,
                                  name="weight", array_annotations={"channel_index": np.arange(len(self._weights[0]))})
        return signal


os.environ['C_LOGS_DICT'] = './logs/'  # Logging folder path
timestep = 1  # Simulation timestep in ms
spike_current = 20  # Synaptic weight required to produce a post-synaptic spike for each pre-synaptic spike received

number_of_bits = 10  # Number of bits in each code word
input_population_size = number_of_bits  # Each input population has one neuron per bit

spike_times_0 = [6,36,59]  # Spike times for neurons in the spike source population "0"
spike_times_1 = [1,26,56]  # Spike times for neurons in the spike source population "1"
spike_not_present_injection_time = [100]  # spike time for neurons that should not emit a spike. The simulation runs up to 75 ms (save_spike_times + 10 ms)
training_times = [29]  # Time at which the teacher neuron emits the training spike
save_spike_times = [65]  # Time at which the Save neuron fires to save to memory the modified synaptic weights
bit_pattern = 0  # Temporary variable used for computation

runtime = save_spike_times[-1] + 10  # Simulation time: 75 ms - This needs to be shorter than the spike_not_present_injection_time variable

# List of bits for each code word to be impressed on the network
bit_pattern_list = []

# User request of the training patterns
input_string = input("Insert number corresponding to bit pattern to train network on, separated by space\n")
user_list = input_string.split()

for i in range(len(user_list)):
    bit_pattern_list.append(int(user_list[i]))

print("The network will be trained on these patterns: ", bit_pattern_list)


# Loop through all the patterns to generate the synaptic weights
for i in range(len(bit_pattern_list)):

    bit_pattern = bit_pattern_list[i]

    # List of spike times for each input neuron for each of the populations
    spike_times_1_array = []
    spike_times_0_array = []
    bit_pattern_string = []

    # These lists are populated on the basis of the code word to train
    for bit_index in range(number_of_bits - 1, -1, -1):
        if (bit_pattern & (1 << bit_index) == 0):
            spike_times_0_array.append(spike_times_0)
            spike_times_1_array.append(spike_not_present_injection_time)
            bit_pattern_string.append('0')
        else:
            spike_times_0_array.append(spike_not_present_injection_time)
            spike_times_1_array.append(spike_times_1)
            bit_pattern_string.append('1')

    print ("")
    print ("**************************")
    print ("**************************")
    print ("Calculating weight changes for pattern {}".format(i))
    print ("Pattern: {}".format(bit_pattern))
    print ("Bit pattern: {}".format(bit_pattern_string))
    print ("**************************")
    print ("**************************")
    print ("")

    print(spike_times_1_array)
    print(spike_times_0_array)

    # Set up the simulator and generate the training network
    # Using the synaptic plasticity nearest-neurghbour spike pair rule
    sim.setup(timestep=timestep)
    sim.set_number_of_neurons_per_core(sim.IF_curr_delta, 100)

    IF_curr_delta_model = sim.IF_curr_delta()
    IF_curr_exp_model = sim.IF_curr_exp()

    ssp_1 = sim.Population(input_population_size, sim.SpikeSourceArray(spike_times_1_array), label='ssp_1')
    ssp_0 = sim.Population(input_population_size, sim.SpikeSourceArray(spike_times_0_array), label='ssp_0')

    save_neuron = sim.Population(1, sim.SpikeSourceArray(save_spike_times), label='save_neuron')

    injector_neurons_exc = sim.Population(input_population_size, IF_curr_delta_model, label='injector_neurons_exc')
    injector_neurons_inh = sim.Population(input_population_size, IF_curr_delta_model, label='injector_neurons_inh')

    teacher_population = sim.Population(1, sim.SpikeSourceArray(training_times), label='teacher_population')

    output_neuron_exc = sim.Population(1, IF_curr_delta_model, label='output_neuron_exc')
    output_neuron_inh = sim.Population(1, IF_curr_delta_model, label='output_neuron_inh')

    static_synapse = sim.StaticSynapse(weight=spike_current, delay=1)
    teaching_synapse = sim.StaticSynapse(weight=spike_current, delay=2)

    source_proj_exc = sim.Projection(ssp_1, injector_neurons_exc, sim.OneToOneConnector(), static_synapse, receptor_type='excitatory')
    source_proj_inh = sim.Projection(ssp_0, injector_neurons_inh, sim.OneToOneConnector(), static_synapse, receptor_type='excitatory')

    save_proj_exc = sim.Projection(save_neuron, injector_neurons_exc, sim.AllToAllConnector(), static_synapse, receptor_type='excitatory')
    save_proj_inh = sim.Projection(save_neuron, injector_neurons_inh, sim.AllToAllConnector(), static_synapse, receptor_type='excitatory')

    training_proj_exc = sim.Projection(teacher_population, output_neuron_exc, sim.AllToAllConnector(), teaching_synapse, receptor_type='excitatory')
    training_proj_inh = sim.Projection(teacher_population, output_neuron_inh, sim.AllToAllConnector(), teaching_synapse, receptor_type='excitatory')

    stdp_model = sim.STDPMechanism(
        timing_dependence=sim.extra_models.SpikeNearestPairRule(tau_plus=5, tau_minus=5, A_plus=1, A_minus=-1),
        weight_dependence=sim.AdditiveWeightDependence(w_min=0, w_max=20),
        weight=0,
        delay=1)

    injector_proj_exc = sim.Projection(injector_neurons_exc, output_neuron_exc, sim.AllToAllConnector(), stdp_model, receptor_type='excitatory')
    injector_proj_inh = sim.Projection(injector_neurons_inh, output_neuron_inh, sim.AllToAllConnector(), stdp_model, receptor_type='inhibitory')

    ssp_1.record(['spikes'])
    ssp_0.record(['spikes'])
    save_neuron.record(['spikes'])
    output_neuron_exc.record(['v','gsyn_exc','spikes'])
    output_neuron_inh.record(['v','gsyn_exc','spikes'])
    teacher_population.record(['spikes'])
    injector_neurons_exc.record(['spikes'])
    injector_neurons_inh.record(['spikes'])

    weight_recorder_exc = WeightRecorder(sampling_interval=1, projection=injector_proj_exc)
    weight_recorder_inh = WeightRecorder(sampling_interval=1, projection=injector_proj_inh)

    # Run the simulation storing also the time evolution of the synaptic weights
    sim.run(runtime, callbacks=[weight_recorder_exc, weight_recorder_inh])

    # Retrieve and save the membrane potential, the excitatory current, the inhibitory current
    # the evolution of the synaptic weights, the input spike trains, the save neuron spike train, the output spike trains
    # and the injector population spike train
    vm_exc = output_neuron_exc.get_data().segments[0].filter(name="v")
    im_exc = output_neuron_exc.get_data().segments[0].filter(name="gsyn_exc")
    spikesm_exc = output_neuron_exc.get_data().segments[0].spiketrains

    vm_inh = output_neuron_inh.get_data().segments[0].filter(name="v")
    im_inh = output_neuron_inh.get_data().segments[0].filter(name="gsyn_exc")
    spikesm_inh = output_neuron_inh.get_data().segments[0].spiketrains

    weights_exc = weight_recorder_exc.get_weights()
    weights_inh = weight_recorder_inh.get_weights()

    ssp1_spikes = ssp_1.get_data().segments[0].spiketrains
    ssp0_spikes = ssp_0.get_data().segments[0].spiketrains
    save_spikes = save_neuron.get_data().segments[0].spiketrains
    spikest = teacher_population.get_data().segments[0].spiketrains

    injector_spikes_exc = injector_neurons_exc.get_data().segments[0].spiketrains
    injector_spikes_inh = injector_neurons_inh.get_data().segments[0].spiketrains

    filename = "saved_data/v_exc_packet{}.pkl".format(i)
    v_file = open(filename, 'wb')
    pkl.dump(vm_exc, v_file)
    v_file.close()

    filename = "saved_data/i_exc_packet{}.pkl".format(i)
    i_file = open(filename, 'wb')
    pkl.dump(im_exc, i_file)
    i_file.close()

    filename = "saved_data/v_inh_packet{}.pkl".format(i)
    v_file = open(filename, 'wb')
    pkl.dump(vm_inh, v_file)
    v_file.close()

    filename = "saved_data/i_inh_packet{}.pkl".format(i)
    i_file = open(filename, 'wb')
    pkl.dump(im_inh, i_file)
    i_file.close()

    filename = "saved_data/weight_exc_final_packet{}.pkl".format(i)
    weight_file = open(filename, 'wb')
    pkl.dump(weights_exc, weight_file)
    weight_file.close()

    filename = "saved_data/weight_inh_final_packet{}.pkl".format(i)
    weight_file = open(filename, 'wb')
    pkl.dump(weights_inh, weight_file)
    weight_file.close()

    filename = "saved_data/ssp1_spikes_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(ssp1_spikes, spike_file)
    spike_file.close()

    filename = "saved_data/ssp0_spikes_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(ssp0_spikes, spike_file)
    spike_file.close()

    filename = "saved_data/save_spikes_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(save_spikes, spike_file)
    spike_file.close()

    filename = "saved_data/injector_spikes_exc_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(injector_spikes_exc, spike_file)
    spike_file.close()

    filename = "saved_data/injector_spikes_inh_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(injector_spikes_inh, spike_file)
    spike_file.close()

    filename = "saved_data/spikest_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(spikest, spike_file)
    spike_file.close()

    filename = "saved_data/spikesm_exc_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(spikesm_exc, spike_file)
    spike_file.close()

    filename = "saved_data/spikesm_inh_packet{}.pkl".format(i)
    spike_file = open(filename, 'wb')
    pkl.dump(spikesm_inh, spike_file)
    spike_file.close()

    # Print to screen all the information retrieved
    print (weights_exc[-1].magnitude)
    print (weights_inh[-1].magnitude)
    print (spikesm_exc)
    print (vm_exc)
    print (im_exc)
    print (spikesm_inh)
    print (vm_inh)
    print (im_inh)
    print (injector_spikes_exc)
    print (injector_spikes_inh)

    # Terminate the simulation and reset the system for the next iteration
    sim.end()
