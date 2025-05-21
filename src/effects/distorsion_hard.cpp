#include <iostream>
#include <math.h>
#include "distorsion_hard.h"
#include "keyvalue.h"

#include <stdlib.h>
#include <cstdio> 

using namespace upc;
using namespace std;

DistorsionHard::DistorsionHard(const std::string &param) {
    KeyValue kv(param);

    if (!kv.to_float("U", U))
      U = 75; // valor por defecto de threshold
  }
  
  void DistorsionHard::command(unsigned int comm) {

  }
  
  void DistorsionHard::operator()(std::vector<float> &x) {
    if (x.empty()) return;

    // 1. Buscar el valor máximo absoluto de la señal
    float max_abs = 0.0f;
    for (float sample : x) {
        float abs_sample = std::abs(sample);
        if (abs_sample > max_abs)
            max_abs = abs_sample;
    }

    if (max_abs == 0.0f) return; // evitar división por cero

    // 2. Calcular el umbral real en función del porcentaje U
    float umbral = (U / 100.0f) * max_abs;

    // 3. Aplicar hard clipping solo si la muestra es diferente de 0
    for (float &sample : x) {
        if (sample == 0.0f) continue;

        if (sample > umbral)
            sample = umbral;
        else if (sample < -umbral)
            sample = -umbral;
    }
  }
  /** 
  void DistorsionHard::operator()(std::vector<float> &x) {
    printf("U = %.6f\n", U);
    for (unsigned int i = 0; i < x.size(); ++i) {
      //hard clipping recortando bruscamente
      printf("x[%u] antes: %.6f\n", i, x[i]);
      if (x[i] == 0.0)
        printf("x[%u] despues: %.6f\n", i, x[i]);
      else if (x[i] > U)
        x[i] = U;
      else if (x[i] < -U)
        x[i] = -U;
      
      printf("x[%u] despues: %.6f\n", i, x[i]);

        // Si está entre [-U, U], no se modifica
    }
  }
    **/