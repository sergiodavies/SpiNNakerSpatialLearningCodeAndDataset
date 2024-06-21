#!/bin/bash

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

mkdir -p saved_data/Single_pattern_992
ipython train_bit_pattern.py << EOF
992
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992
EOF

mv saved_data/*.pkl saved_data/Single_pattern_992/
