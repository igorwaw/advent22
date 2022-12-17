#ifndef MAP_H
#define MAP_H

#include <iostream>
#include <vector>

const int16_t max_d=9999; // maximum route length

using Mappoint = std::pair<int16_t,int16_t>;



class Map {
	public:
	  Map(const char*  filename);
	  void print(bool full=false);
	  void print_dijkstra();
	  char getelevation(Mappoint p) {return mapbuffer[p.second][p.first]; }
	  int16_t getdistance(Mappoint p) {return disbuffer[p.second][p.first]; }
	  void setdistance(Mappoint p, int16_t distance) { disbuffer[p.second][p.first] = distance; };
	  Mappoint getstart() { return start; }
	  Mappoint getend() { return end; }
	  int16_t getwidth() { return width; }
	  int16_t getheight() { return height; }
	private:
	  std::vector<std::string> mapbuffer;
	  std::vector<std::vector<int16_t> > disbuffer;
	  int16_t width, height;
	  Mappoint start;
	  Mappoint end;
	  void setelevation(Mappoint p, char elevation) { mapbuffer[p.second][p.first] = elevation; };
};


#endif
