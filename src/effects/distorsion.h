#ifndef DISTORSION_H
#define DISTORSION_H

#include <vector>
#include <string>
#include "effect.h"

namespace upc {
  class Distorsion: public upc::Effect {
    private:
      float G; //G de Gain, ganancia
    public:
      Distorsion(const std::string &param = "");
	  void operator()(std::vector<float> &x);
	  void command(unsigned int);
  };
}

#endif