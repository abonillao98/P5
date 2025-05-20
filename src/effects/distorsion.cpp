#include <iostream>
#include <math.h>
#include "distorsion.h"
#include "keyvalue.h"

#include <stdlib.h>

using namespace upc;
using namespace std;

Distorsion::Distorsion(const std::string &param) {
    KeyValue kv(param);

    if (!kv.to_float("G", G))
      G = 5.0; // valor por defecto de ganancia
  }
  
  void Distorsion::command(unsigned int comm) {
    if (comm == 1) G = 0;
  }
  
  void Distorsion::operator()(std::vector<float> &x) {
    for (unsigned int i = 0; i < x.size(); ++i) {
      // Soft clipping usando tangente hiperbólica
      x[i] = tanh(G * x[i]);
    }
  }