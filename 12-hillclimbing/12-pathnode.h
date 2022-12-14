#ifndef PATHNODE_H
#define PATHNODE_H

#include <memory>
#include <iostream>
#include "12-map.h"


enum DIRECTION {top, bottom, left, right};

class Pathnode {
	public:
	  Pathnode(Mappoint newcoords, int16_t dd=0) : coords(newcoords), depth(dd)  {}
	  void print();
	  void addchild(DIRECTION dir);
	  void printtree();
      int16_t getdepth() { return depth; }
      Mappoint getcoords() { return coords; }
      
	  std::shared_ptr<Pathnode> child[4];
	  
	  
	private:
	  int16_t depth;
	  Mappoint coords;
	  
};



#endif
