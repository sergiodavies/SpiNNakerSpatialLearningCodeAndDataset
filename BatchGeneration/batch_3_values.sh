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

mkdir -p saved_data/Multiple_patterns_0+0+0
ipython train_bit_pattern.py << EOF
0 0 0
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 0
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+0/


mkdir -p saved_data/Multiple_patterns_0+0+1
ipython train_bit_pattern.py << EOF
0 0 1
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 1
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+1/


mkdir -p saved_data/Multiple_patterns_0+0+3
ipython train_bit_pattern.py << EOF
0 0 3
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 3
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+3/


mkdir -p saved_data/Multiple_patterns_0+0+7
ipython train_bit_pattern.py << EOF
0 0 7
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 7
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+7/


mkdir -p saved_data/Multiple_patterns_0+0+15
ipython train_bit_pattern.py << EOF
0 0 15
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 15
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+15/


mkdir -p saved_data/Multiple_patterns_0+0+31
ipython train_bit_pattern.py << EOF
0 0 31
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 31
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+31/


mkdir -p saved_data/Multiple_patterns_0+0+63
ipython train_bit_pattern.py << EOF
0 0 63
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 63
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+63/


mkdir -p saved_data/Multiple_patterns_0+0+127
ipython train_bit_pattern.py << EOF
0 0 127
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 127
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+127/


mkdir -p saved_data/Multiple_patterns_0+0+255
ipython train_bit_pattern.py << EOF
0 0 255
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 255
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+255/


mkdir -p saved_data/Multiple_patterns_0+0+511
ipython train_bit_pattern.py << EOF
0 0 511
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 511
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+511/


mkdir -p saved_data/Multiple_patterns_0+0+1023
ipython train_bit_pattern.py << EOF
0 0 1023
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 0 1023
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+0+1023/


mkdir -p saved_data/Multiple_patterns_0+1+2
ipython train_bit_pattern.py << EOF
0 1 2
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 2
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+2/


mkdir -p saved_data/Multiple_patterns_0+1+6
ipython train_bit_pattern.py << EOF
0 1 6
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 6
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+6/


mkdir -p saved_data/Multiple_patterns_0+1+14
ipython train_bit_pattern.py << EOF
0 1 14
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 14
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+14/


mkdir -p saved_data/Multiple_patterns_0+1+30
ipython train_bit_pattern.py << EOF
0 1 30
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 30
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+30/


mkdir -p saved_data/Multiple_patterns_0+1+62
ipython train_bit_pattern.py << EOF
0 1 62
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 62
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+62/


mkdir -p saved_data/Multiple_patterns_0+1+126
ipython train_bit_pattern.py << EOF
0 1 126
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 126
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+126/


mkdir -p saved_data/Multiple_patterns_0+1+254
ipython train_bit_pattern.py << EOF
0 1 254
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 254
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+254/


mkdir -p saved_data/Multiple_patterns_0+1+510
ipython train_bit_pattern.py << EOF
0 1 510
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 510
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+510/


mkdir -p saved_data/Multiple_patterns_0+1+1022
ipython train_bit_pattern.py << EOF
0 1 1022
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 1 1022
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+1+1022/


mkdir -p saved_data/Multiple_patterns_0+3+5
ipython train_bit_pattern.py << EOF
0 3 5
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 5
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+5/


mkdir -p saved_data/Multiple_patterns_0+3+12
ipython train_bit_pattern.py << EOF
0 3 12
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 12
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+12/


mkdir -p saved_data/Multiple_patterns_0+3+13
ipython train_bit_pattern.py << EOF
0 3 13
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 13
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+13/


mkdir -p saved_data/Multiple_patterns_0+3+28
ipython train_bit_pattern.py << EOF
0 3 28
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 28
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+28/


mkdir -p saved_data/Multiple_patterns_0+3+29
ipython train_bit_pattern.py << EOF
0 3 29
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 29
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+29/


mkdir -p saved_data/Multiple_patterns_0+3+60
ipython train_bit_pattern.py << EOF
0 3 60
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 60
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+60/


mkdir -p saved_data/Multiple_patterns_0+3+61
ipython train_bit_pattern.py << EOF
0 3 61
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 61
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+61/


mkdir -p saved_data/Multiple_patterns_0+3+124
ipython train_bit_pattern.py << EOF
0 3 124
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 124
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+124/


mkdir -p saved_data/Multiple_patterns_0+3+125
ipython train_bit_pattern.py << EOF
0 3 125
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 125
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+125/


mkdir -p saved_data/Multiple_patterns_0+3+252
ipython train_bit_pattern.py << EOF
0 3 252
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 252
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+252/


mkdir -p saved_data/Multiple_patterns_0+3+253
ipython train_bit_pattern.py << EOF
0 3 253
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 253
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+253/


mkdir -p saved_data/Multiple_patterns_0+3+508
ipython train_bit_pattern.py << EOF
0 3 508
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 508
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+508/


mkdir -p saved_data/Multiple_patterns_0+3+509
ipython train_bit_pattern.py << EOF
0 3 509
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 509
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+509/


mkdir -p saved_data/Multiple_patterns_0+3+1020
ipython train_bit_pattern.py << EOF
0 3 1020
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 1020
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+1020/


mkdir -p saved_data/Multiple_patterns_0+3+1021
ipython train_bit_pattern.py << EOF
0 3 1021
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 3 1021
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+3+1021/


mkdir -p saved_data/Multiple_patterns_0+7+25
ipython train_bit_pattern.py << EOF
0 7 25
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 25
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+25/


mkdir -p saved_data/Multiple_patterns_0+7+56
ipython train_bit_pattern.py << EOF
0 7 56
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 56
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+56/


mkdir -p saved_data/Multiple_patterns_0+7+57
ipython train_bit_pattern.py << EOF
0 7 57
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 57
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+57/


mkdir -p saved_data/Multiple_patterns_0+7+120
ipython train_bit_pattern.py << EOF
0 7 120
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 120
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+120/


mkdir -p saved_data/Multiple_patterns_0+7+121
ipython train_bit_pattern.py << EOF
0 7 121
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 121
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+121/


mkdir -p saved_data/Multiple_patterns_0+7+248
ipython train_bit_pattern.py << EOF
0 7 248
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 248
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+248/


mkdir -p saved_data/Multiple_patterns_0+7+249
ipython train_bit_pattern.py << EOF
0 7 249
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 249
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+249/


mkdir -p saved_data/Multiple_patterns_0+7+504
ipython train_bit_pattern.py << EOF
0 7 504
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 504
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+504/


mkdir -p saved_data/Multiple_patterns_0+7+505
ipython train_bit_pattern.py << EOF
0 7 505
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 505
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+505/


mkdir -p saved_data/Multiple_patterns_0+7+1016
ipython train_bit_pattern.py << EOF
0 7 1016
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 1016
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+1016/


mkdir -p saved_data/Multiple_patterns_0+7+1017
ipython train_bit_pattern.py << EOF
0 7 1017
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 7 1017
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+7+1017/


mkdir -p saved_data/Multiple_patterns_0+15+51
ipython train_bit_pattern.py << EOF
0 15 51
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 51
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+51/


mkdir -p saved_data/Multiple_patterns_0+15+113
ipython train_bit_pattern.py << EOF
0 15 113
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 113
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+113/


mkdir -p saved_data/Multiple_patterns_0+15+240
ipython train_bit_pattern.py << EOF
0 15 240
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 240
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+240/


mkdir -p saved_data/Multiple_patterns_0+15+115
ipython train_bit_pattern.py << EOF
0 15 115
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 115
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+115/


mkdir -p saved_data/Multiple_patterns_0+15+241
ipython train_bit_pattern.py << EOF
0 15 241
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 241
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+241/


mkdir -p saved_data/Multiple_patterns_0+15+496
ipython train_bit_pattern.py << EOF
0 15 496
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 496
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+496/


mkdir -p saved_data/Multiple_patterns_0+15+243
ipython train_bit_pattern.py << EOF
0 15 243
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 243
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+243/


mkdir -p saved_data/Multiple_patterns_0+15+497
ipython train_bit_pattern.py << EOF
0 15 497
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 497
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+497/


mkdir -p saved_data/Multiple_patterns_0+15+1008
ipython train_bit_pattern.py << EOF
0 15 1008
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 1008
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+1008/


mkdir -p saved_data/Multiple_patterns_0+15+499
ipython train_bit_pattern.py << EOF
0 15 499
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 499
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+499/


mkdir -p saved_data/Multiple_patterns_0+15+1009
ipython train_bit_pattern.py << EOF
0 15 1009
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 1009
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+1009/


mkdir -p saved_data/Multiple_patterns_0+15+1011
ipython train_bit_pattern.py << EOF
0 15 1011
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 15 1011
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+15+1011/


mkdir -p saved_data/Multiple_patterns_0+31+227
ipython train_bit_pattern.py << EOF
0 31 227
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 31 227
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+31+227/


mkdir -p saved_data/Multiple_patterns_0+31+481
ipython train_bit_pattern.py << EOF
0 31 481
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 31 481
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+31+481/


mkdir -p saved_data/Multiple_patterns_0+31+992
ipython train_bit_pattern.py << EOF
0 31 992
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 31 992
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+31+992/


mkdir -p saved_data/Multiple_patterns_0+31+483
ipython train_bit_pattern.py << EOF
0 31 483
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 31 483
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+31+483/


mkdir -p saved_data/Multiple_patterns_0+31+993
ipython train_bit_pattern.py << EOF
0 31 993
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 31 993
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+31+993/


mkdir -p saved_data/Multiple_patterns_0+31+995
ipython train_bit_pattern.py << EOF
0 31 995
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 31 995
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+31+995/


mkdir -p saved_data/Multiple_patterns_0+63+455
ipython train_bit_pattern.py << EOF
0 63 455
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 63 455
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+63+455/


mkdir -p saved_data/Multiple_patterns_0+63+963
ipython train_bit_pattern.py << EOF
0 63 963
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 63 963
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+63+963/


mkdir -p saved_data/Multiple_patterns_0+63+967
ipython train_bit_pattern.py << EOF
0 63 967
EOF

ipython weight_processing.py
ipython homeostasis.py << EOF && ipython testing.py
0 63 967
EOF

mv saved_data/*.pkl saved_data/Multiple_patterns_0+63+967/


