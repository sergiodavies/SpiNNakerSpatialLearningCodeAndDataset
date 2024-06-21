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
#include <map>
#include <tuple>

int hammingDistance(int n1, int n2)
{
    int x = n1 ^ n2;
    int setBits = 0;

    while (x > 0) {
        setBits += x & 1;
        x >>= 1;
    }

    return setBits;
}

int main()
{
  std::map<std::tuple<int, int, int>, std::tuple<int, int, int>> HDmap;

  int cw0 = 0;
  int cw1 = 0;
  int cw2 = 0;

  for (cw0 = 0; cw0 < 1024; cw0++)
  {
    for (cw1 = 0; cw1 < 1024; cw1++)
    {
      for (cw2 = 0; cw2 < 1024; cw2++)
      {
        int HD01 = hammingDistance(cw0, cw1);
        int HD02 = hammingDistance(cw0, cw2);
        int HD12 = hammingDistance(cw1, cw2);

        std::tuple<int, int, int> HDTuple(HD01, HD02, HD12);
        std::tuple<int, int, int> CWTuple(cw0, cw1, cw2);

        auto search = HDmap.find(HDTuple);
        if (search == HDmap.end())
        {
          printf ("Inserting: %d, %d, %d\n", std::get<0>(CWTuple), std::get<1>(CWTuple), std::get<2>(CWTuple));
          HDmap.emplace(std::make_pair(HDTuple, CWTuple));
        }
        else
        {
          printf ("Not inserting: %d, %d, %d\n", std::get<0>(CWTuple), std::get<1>(CWTuple), std::get<2>(CWTuple));
        }
      }
    }
  }

  FILE *FMapOutput = fopen("HDMap.csv", "w");
  fprintf(FMapOutput, "HD01, HD02, HD12, CW0, CW1, CW2\n");
  for (auto it = HDmap.begin(); it != HDmap.end(); ++it) {
      fprintf(FMapOutput, "%d, %d, %d, %d, %d, %d\n", std::get<0>(it->first), std::get<1>(it->first), std::get<2>(it->first), std::get<0>(it->second), std::get<1>(it->second), std::get<2>(it->second));
  }
  fclose(FMapOutput);

  return 0;
}
