#ifndef DISTORSION_HARD_H
#define DISTORSION_HARD_H

#include <vector>
#include <string>
#include "effect.h"

namespace upc {
  class DistorsionHard: public upc::Effect {
    private:
      float U; //U de umbral, threshold
    public:
      DistorsionHard(const std::string &param = "");
	  void operator()(std::vector<float> &x);
	  void command(unsigned int);
  };
}

#endif