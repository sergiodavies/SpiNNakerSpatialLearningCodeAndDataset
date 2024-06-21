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

mkdir -p saved_data/Multiple_patterns_992+1008
ipython train_bit_pattern.py << EOF
992 1008
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 1008
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+1008/


mkdir -p saved_data/Multiple_patterns_992+1016
ipython train_bit_pattern.py << EOF
992 1016
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 1016
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+1016/


mkdir -p saved_data/Multiple_patterns_992+1020
ipython train_bit_pattern.py << EOF
992 1020
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 1020
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+1020/


mkdir -p saved_data/Multiple_patterns_992+1022
ipython train_bit_pattern.py << EOF
992 1022
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 1022
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+1022/


mkdir -p saved_data/Multiple_patterns_992+1023
ipython train_bit_pattern.py << EOF
992 1023
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 1023
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+1023/


mkdir -p saved_data/Multiple_patterns_992+960
ipython train_bit_pattern.py << EOF
992 960
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 960
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+960/


mkdir -p saved_data/Multiple_patterns_992+896
ipython train_bit_pattern.py << EOF
992 896
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 896
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+896/


mkdir -p saved_data/Multiple_patterns_992+768
ipython train_bit_pattern.py << EOF
992 768
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 768
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+768/


mkdir -p saved_data/Multiple_patterns_992+512
ipython train_bit_pattern.py << EOF
992 512
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 512
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+512/


mkdir -p saved_data/Multiple_patterns_992+0
ipython train_bit_pattern.py << EOF
992 0
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 0
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+0/


mkdir -p saved_data/Multiple_patterns_992+16
ipython train_bit_pattern.py << EOF
992 16
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 16
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+16/


mkdir -p saved_data/Multiple_patterns_992+24
ipython train_bit_pattern.py << EOF
992 24
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 24
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+24/


mkdir -p saved_data/Multiple_patterns_992+28
ipython train_bit_pattern.py << EOF
992 28
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 28
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+28/


mkdir -p saved_data/Multiple_patterns_992+30
ipython train_bit_pattern.py << EOF
992 30
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 30
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+30/


mkdir -p saved_data/Multiple_patterns_992+31
ipython train_bit_pattern.py << EOF
992 31
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
992 31
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_992+31/


