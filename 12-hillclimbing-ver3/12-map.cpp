#include "12-map.h"
#include <cstring>
#include <iostream>


std::ostream&  operator<< (std::ostream& stream, const Mappoint p) {
	stream<<p.x<<','<<p.y; 
	return stream;
} 


void Map::print(bool full) {
	std::cout<<"Map width: " <<+width<<" height "<<+height<<'\n';
	std::cout<<"Starting point: " <<+start.x<<','<<+start.y;
	std::cout<<"   Ending point: " <<+end.x<<','<<+end.y<<"\n\n";
	if (full) {
		for (int j=0;j<height;++j) {
			for (int i=0;i<width;++i)  
				std::cout<<getelevation(Mappoint(i,j));
			std::cout<<'\n';
		}
		std::cout<<"----------------------------------\n";
	}
}

void Map::print_dijkstra() {
	std::cout<<"Map width: " <<+width<<" height "<<+height<<'\n';
	std::cout<<"Starting point: " <<+start.x<<','<<+start.y;
	std::cout<<"   Ending point: " <<+end.x<<','<<+end.y<<"\n\n";
	for (int j=0;j<height;++j) {
		for (int i=0;i<width;++i)  
			printf("%04i ", getdistance(Mappoint(i,j)) );
		std::cout<<'\n';
	}

}


Map::~Map() {
	delete mapbuffer;
	delete disbuffer;
}


Map::Map(const char* filename) {
	FILE* mapfile = fopen(filename, "r"); // Opening file in reading mode
    if (!mapfile) 
        throw std::runtime_error("Cannot open file");

    // check file size
    fseek(mapfile, 0, SEEK_END); // seek to end of file
    int filesize = ftell(mapfile); 
    fseek(mapfile, 0, SEEK_SET); // seek back to beginning of file
    //check line width
	char c;
    while ( (c=getc(mapfile)) != EOF ) {
        if (c=='\n')
            break;
        ++width;
    }
    fseek(mapfile, 0, SEEK_SET); // seek back to beginning of file
    //height can be calculated
    height=filesize/(width+1); // +1 for \n at the end of every line
    mapbuffer=new char[filesize];
    disbuffer=new int16_t[filesize];
    char tempstring[width+1]; // +1 for \n at the end of every line
    for (int16_t i=0; i<height; ++i) {
		fgets(tempstring,width+2,mapfile);
		memcpy(mapbuffer+i*width, tempstring, width);
	}
	fclose(mapfile);
	
	// set start and end points, initialize Dijkstra value
	for (int16_t i=0;i<width;++i) {
		for (int16_t j=0;j<height;++j) {
			setdistance(Mappoint(i,j),max_d);
			c=getelevation(Mappoint(i,j));
			if (c=='S') {
				setelevation(Mappoint(i,j),'a');
				setdistance(Mappoint(i,j),0);
				start.x=i;
				start.y=j;
			}
			if (c=='E') {
				setelevation(Mappoint(i,j),'z');
				end.x=i;
				end.y=j;
			}
		}
	}
}
