#include <iostream>
#include <math.h>
#include "distorsion_tanh.h"
#include "keyvalue.h"

#include <stdlib.h>
#include <cstdio> 

using namespace upc;
using namespace std;

DistorsionTanh::DistorsionTanh(const std::string &param) {
    KeyValue kv(param);

    if (!kv.to_float("G", G))
      G = 5.0; // valor por defecto de ganancia
  }
  
  void DistorsionTanh::command(unsigned int comm) {
    //if (comm == 1) phase = 0;
  }
  
  void DistorsionTanh::operator()(std::vector<float> &x) {
    //G = 5.0;
    //printf("G = %.6f\n", G);

    for (unsigned int i = 0; i < x.size(); ++i) {
      // Soft clipping usando tangente hiperbólica
      //printf("x[%u] antes: %.6f\n", i, x[i]);
      x[i] = tanh(G * x[i]); 
      //printf("x[%u] despues: %.6f\n", i, x[i]);
    }
  }