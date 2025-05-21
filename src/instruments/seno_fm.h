#ifndef SENO_FM
#define SENO_FM

#include <vector>
#include <string>
#include "instrument.h"
#include "envelope_adsr.h"

namespace upc {
  class seno_fm: public upc::Instrument {
    EnvelopeADSR adsr;
    std::vector<float> x;
    float A;
    float fc, fm;
    float Ic;       // índice real (en radianes)
    float phase_c, phase_m;
    float inc_c, inc_m;
  public:
    seno_fm(const std::string &param = "");
    void command(long cmd, long note, long velocity=1); 
    const std::vector<float> & synthesize();
    bool is_active() const { return bActive; }
  };
}

#endif
