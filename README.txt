This folder contains all the software and data used in the preparation of the
article by:


Davies S., Gait A., Rowley A., and Di Nuovo A.
"Supervised Learning of Spatial Features with STDP and Homeostasis Using
Spiking Neural Networks on SpiNNaker"


The data and code are subject to the CC BY license, which can be found in the
LICENSE.txt file within the same folder.

If this software or data is used in derived publications, a citation to the
mentioned article is appreciated by the authors.

The software is designed to run on the SpiNNaker system. To install the
relevant software, please check the instructions at:
https://spinnakermancehster.github.io/

The code used for this publication is drawn directly from git repositories.
The latest commit of the repositories used are:
https://github.com/SpiNNakerManchester/spalloc/commit/d147e4cb57334c64540c50f78752c73dc33ea985
https://github.com/SpiNNakerManchester/PACMAN/commit/6b2236a1a081fc4c82018705109f69b3cfd8798c
https://github.com/SpiNNakerManchester/SpiNNMachine/commit/44cf90485e137a55e042a4be4969ddddf9522426
https://github.com/SpiNNakerManchester/SpiNNMan/commit/ab9fcdfe347d065e8c7f52fe17775ac39eedcced
https://github.com/SpiNNakerManchester/SpiNNUtils/commit/ae7c045885439d6443ea26ea9e552e13a9c8d33e
https://github.com/SpiNNakerManchester/sPyNNaker/commit/1319cea0d8c2f5310c67db70a072661ad0b26058
https://github.com/SpiNNakerManchester/SpiNNFrontEndCommon/commit/901521815c65ef0b726fa939b15b8593e5fecb9b
https://github.com/SpiNNakerManchester/spinn_common/commit/fa5f769a7e8bab42b6932557c0deaebc1d7f2016
https://github.com/SpiNNakerManchester/spinnaker_tools/commit/26dd8651d7af8371ca1d5927524d1af2527dd041
https://github.com/SpiNNakerManchester/SpiNNakerGraphFrontEnd/commit/17769a81bd0f047b96d91f19d570c2d5887f490b
https://github.com/HumanBrainProject/ebrains-drive/commit/3be240da78b23488cf01dc9768423bb962673c8d

The PyNN interface used is downloaded from the link below and has version 0.11.0:
https://files.pythonhosted.org/packages/source/P/PyNN/PyNN-0.11.0.tar.gz

Although it has not been tested, this code should also work with the most
recent sPyNNaker release on PyPI (v7.1.0) and with the upcoming version (8.0)
that will be distributed through PyPI.

All code has been run on Python 3.12 using the IPython command shell. The
IPython interface is required to run this code.

The files are saved in Pickle format, which is a serialisation library
included in this version of Python.
https://docs.python.org/3.12/library/pickle.html
For completeness and future reference, this specific version of the
Pickle library is included in this folder in the file pickle.py.



Data shared:

 - saved_data/One pattern - Information recorded from the simulation of a
                            spiking neural network trained on a single pattern

 - saved_data/Two patterns - Information recorded from the simulation of a
                             spiking neural network trained on two patterns

 - saved_data/Three patterns - Information recorded from the simulation of a
                               spiking neural network trained on three patterns

 - Graphs - The 3D graphs presented in the article


Code shared:

 - BatchGeneration - Code used to generate large simulation batches for testing
                     the spiking neural network with two and three trained
                     patterns

 - HammingDistance - Code used to compute the Hamming Distance between all
                     combination of numbers in the range 0 - 1023

 - batch_1_value.sh - Batch file which runs the spiking neural network
                      simulation, trains the network on a single pattern, and
                      retrieves all the information required to extract the
                      metrics relevant to the publication at the end of the
                      simulation.

 - batch_2_values.sh - Batch file which runs the spiking neural network
                       simulation, trains the network on two patterns, and
                       retrieves all the information required to extract the
                       metrics relevant to the publication at the end of the
                       simulation.


 - batch_3_values.sh - Batch file which runs the spiking neural network
                       simulation, trains the network on three patterns, and
                       retrieves all the information required to extract the
                       metrics relevant to the publication at the end of the
                       simulation.

 - metric_extractions_1.py - Python script that extracts the metrics relevant
                             to the publication from the simulations in the
                             folder saved_data/One pattern. The extracted
                             metrics are written to the file
                             "output_metrics_1.csv".

 - metric_extractions_2.py - Python script that extracts the metrics relevant
                             to the publication from the simulations in the
                             folder saved_data/Two patterns. The extracted
                             metrics are written to the file
                             "output_metrics_2.csv".

 - metric_extractions_3_graphics.py -
   Python script that extracts the metrics relevant to the publication from the
   simulations in the folder saved_data/Three patterns. The extracted metrics
   are written to the file "output_metrics_3.csv". This script also generates
   the graphs used in Figure 6 of the paper.


 - output_metrics_1.csv - Metrics extracted from the simulation of a spiking
                          neural network trained on a single pattern.

 - output_metrics_2.csv - Metrics extracted from the simulation of a spiking
                          neural network trained on two patterns.

 - output_metrics_2.ods - Similar to the above, but data is reorganised
                          accordingly to the publication requirements

 - output_metrics_3.csv - Metrics extracted from the simulation of a spiking
                          neural network trained on three patterns.

 - output_metrics_3.ods - Similar to the above, but data is reorganised
                          accordingly to the publication requirements


 - train_bit_pattern.py - This script is used to train a spiking neural
                          network on one or more patterns. The script prompts
                          the user to input the patterns to be impressed on
                          the network. The outcome of this training is placed
                          in the saved_data folder in pickle file format,
                          which is commonly used in Python.

 - weight_processing.py - This script is used to post-process the synaptic
                          weights after the network has been trained. Input
                          files are in pickle format from the saved_data
                          folder. The output is stored in the same saved_data
                          folder.

 - homeostasis.py - This script calculates the homeostatic value needed to
                    adjust the synaptic weights, ensuring the output neuron
                    fires at most once for the correct input pattern(s). The
                    code prompts the user to input the pattern(s) to be
                    checked. The homeostatic value is searched within the
                    range of 0 to 100.

 - testing.py - This script tests the network with all possible input
                patterns. Twenty-five patterns are tested simultaneously
                across 25 identical networks running in parallel on the
                SpiNNaker system. The output of these simulations is stored in
                the saved_data folder.

 - pickle.py - Pickle file library included in Python 3.12. This is present
               here for future reference. Information on this library is
               available at:
               https://docs.python.org/3.12/library/pickle.html


Additional folders present:

 - logs
 - reports

Although these folders are empty, they are required to run the simulation
software within the current folder.
