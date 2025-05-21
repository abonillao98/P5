#ifndef DISTORSION_TANH_H
#define DISTORSION_TANH_H

#include <vector>
#include <string>
#include "effect.h"

namespace upc {
  class DistorsionTanh: public upc::Effect {
    private:
      float G; //G de Gain, ganancia. Entre 1.0 y 5.0
    public:
      DistorsionTanh(const std::string &param = "");
	  void operator()(std::vector<float> &x);
	  void command(unsigned int);
  };
}

#endif