#ifndef MAP_H
#define MAP_H

#include <iostream>

const int16_t max_d=1000; // maximum route length

struct Mappoint {
	int16_t x;
	int16_t y;
	Mappoint(int16_t xx, int16_t yy): x(xx), y(yy) {}
	Mappoint(): x(0), y(0) {}
	//Mappoint(Mappoint &p): x(p.x), y(p.y) {}
	//Mappoint& operator=(const Mappoint p) {x=p.x; y=p.y;return *this; }
	bool operator==( const Mappoint& rhs) { return ( x==rhs.x and y==rhs.y ); }
    friend std::ostream&  operator<< (std::ostream& stream, const Mappoint p);
};


class Map {
	public:
	  Map(const char*  filename);
	  ~Map();
	  void print(bool full=false);
	  void print_dijkstra();
	  char getelevation(Mappoint p) {return *(mapbuffer+p.y*width+p.x); }
	  int16_t getdistance(Mappoint p) {return *( disbuffer+ (p.y*width+p.x)*sizeof(int16_t) ); }
	  void setdistance(Mappoint p, int16_t distance) { *( disbuffer+ (p.y*width+p.x)*sizeof(int16_t) ) = distance; };
	  Mappoint getstart() { return start; }
	  Mappoint getend() { return end; }
	  int16_t getwidth() { return width; }
	  int16_t getheight() { return height; }
	private:
	  char* mapbuffer; // holds map = elevation of each point
	  int16_t* disbuffer; // holds distance from start for each point
	  int16_t width, height;
	  Mappoint start;
	  Mappoint end;
	  void setelevation(Mappoint p, char elevation) { *(mapbuffer+p.y*width+p.x) = elevation; };
};


#endif
