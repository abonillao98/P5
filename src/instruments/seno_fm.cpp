#include <iostream>
#include <math.h>
#include "seno_fm.h"
#include "keyvalue.h"

#include <stdlib.h>

using namespace upc;
using namespace std;

seno_fm::seno_fm(const std::string &param)
  : adsr(SamplingRate, param) {
  x.resize(BSIZE);
  bActive = false;

  KeyValue kv(param);
  int N1 = 1, N2 = 1;
  float I = 0;

  kv.to_int("N1", N1);
  kv.to_int("N2", N2);
  kv.to_float("I", I);

  // Las frecuencias y el índice se asignan en command() porque dependen de la nota
  fm = N2;  // Proporción, f0 se multiplicará luego
  fc = N1;
  Ic = I; // Se transformará luego a índice real
}

void seno_fm::command(long cmd, long note, long velocity) {
  if (cmd == 9) {
    bActive = true;
    adsr.start();
    A = velocity / 127.0f;

    float f0 = 440.0f * pow(2.0, (note - 69) / 12.0);
    float delta_f = f0 * (pow(2.0, Ic / 12.0) - 1.0);

    fm = f0 * fm;  // convertir de proporción a Hz
    fc = f0 * fc;

    inc_c = 2 * M_PI * fc / SamplingRate;
    inc_m = 2 * M_PI * fm / SamplingRate;

    Ic = 2 * M_PI * delta_f / fm;  // índice de modulación real

    phase_c = 0.0;
    phase_m = 0.0;
  }
  else if (cmd == 8)
    adsr.stop();
  else if (cmd == 0)
    adsr.end();
}

const std::vector<float> & seno_fm::synthesize() {
  if (!adsr.active()) {
    x.assign(x.size(), 0);
    bActive = false;
    return x;
  }
  else if (!bActive)
    return x;

  for (unsigned int i = 0; i < x.size(); ++i) {
    phase_m += inc_m;
    phase_c += inc_c + Ic * sin(phase_m);

    // Normalizar fases
    if (phase_m > 2 * M_PI) phase_m -= 2 * M_PI;
    if (phase_c > 2 * M_PI) phase_c -= 2 * M_PI;

    x[i] = A * sin(phase_c);
  }

  adsr(x);
  return x;
}