// This document contains software used in the preparation of the
// article by:
//
// Davies S., Gait A., Rowley A., and Di Nuovo A.
// "Supervised Learning of Spatial Features with STDP and Homeostasis Using
// Spiking Neural Networks on SpiNNaker"
//
// The data and code are subject to the CC BY license, which can be found in the
// LICENSE.txt file within the same folder.
//
// If this software or data is used in derived publications, a citation to the
// mentioned article is appreciated by the authors.

#include <stdio.h>

int main()
{
    FILE *csvSource = fopen("2values_to_test.csv", "r");
    FILE *batchOutput = fopen("batch_2_values.sh", "w");

    char columnHeaders[256];

    fprintf (batchOutput, "#!/bin/bash\n\n");

    fprintf (batchOutput, "# This document contains software used in the preparation of the\n");
    fprintf (batchOutput, "# article by:\n");
    fprintf (batchOutput, "#\n");
    fprintf (batchOutput, "# Davies S., Gait A., Rowley A., and Di Nuovo A.\n");
    fprintf (batchOutput, "# \"Supervised Learning of Spatial Features with STDP and Homeostasis Using\n");
    fprintf (batchOutput, "# Spiking Neural Networks on SpiNNaker\"\n");
    fprintf (batchOutput, "#\n");
    fprintf (batchOutput, "# The data and code are subject to the CC BY license, which can be found in the\n");
    fprintf (batchOutput, "# LICENSE.txt file within the same folder.\n");
    fprintf (batchOutput, "#\n");
    fprintf (batchOutput, "# If this software or data is used in derived publications, a citation to the\n");
    fprintf (batchOutput, "# mentioned article is appreciated by the authors.\n");
    fprintf (batchOutput, "\n");

    fgets(columnHeaders, 256, csvSource);

    for(;;)
    {
        int cw0, cw1;
        int ret = 0;
        char foldername[256];

        ret = fscanf(csvSource, "%*d,%d,%d\n", &cw0, &cw1);

        if (ret != 2)
            break;

        snprintf (foldername, 256, "saved_data/Multiple_patterns_%d+%d", cw0, cw1);
        fprintf (batchOutput, "mkdir -p %s\n", foldername);
        fprintf (batchOutput, "ipython train_bit_pattern.py << EOF\n");
        fprintf (batchOutput, "%d %d\n", cw0, cw1);
        fprintf (batchOutput, "EOF\n\n");
        fprintf (batchOutput, "ipython weight_processing.py\n");
        fprintf (batchOutput, "ipython homeostasis.py << EOF && ipython testing.py\n");
        fprintf (batchOutput, "%d %d\n", cw0, cw1);
        fprintf (batchOutput, "EOF\n\n");
        fprintf (batchOutput, "mv saved_data/*.pkl %s/\n\n\n", foldername);

    }
    fclose(csvSource);
    fclose(batchOutput);
}



