#ifndef MAP_H
#define MAP_H

#include <iostream>

struct Mappoint {
	int16_t x;
	int16_t y;
	Mappoint(int16_t xx, int16_t yy): x(xx), y(yy) {}
	Mappoint(): x(0), y(0) {}
	bool operator==( const Mappoint& rhs) { return ( x==rhs.x and y==rhs.y ); }
    friend std::ostream&  operator<< (std::ostream& stream, const Mappoint p);
};


class Map {
	public:
	  Map(const char*  filename);
	  ~Map();
	  void print(bool full=false);
	  char getelevation(Mappoint p) {return *(mapbuffer+p.y*width+p.x); }
	  Mappoint getstart() { return start; }
	  Mappoint getend() { return end; }
	  int16_t getwidth() { return width; }
	  int16_t getheight() { return height; }
	private:
	  char* mapbuffer;
	  int16_t width, height;
	  Mappoint start;
	  Mappoint end;
	  void setelevation(Mappoint p, char elevation) { *(mapbuffer+p.y*width+p.x) = elevation; };
};


#endif
