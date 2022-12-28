#include "12-map.h"
#include <cstring>
#include <iostream>
#include <fstream>



void Map::print(bool full) {
	std::cout<<"Map width: " <<+width<<" height "<<+height<<'\n';
	std::cout<<"Starting point: " <<+start.first<<','<<+start.second;
	std::cout<<"   Ending point: " <<+end.first<<','<<+end.second<<"\n\n";
	if (full) {  // printing map character by character to make sure other functions doing similar adressing work properly
		for (int j=0;j<height;++j) {
			for (int i=0;i<width;++i)  
				std::cout<<getelevation(Mappoint(i,j));
			std::cout<<'\n';
		}
		std::cout<<"----------------------------------\n";
	}
}

std::vector<Mappoint> Map::getPointsByElevation(char elevation) {
	std::vector<Mappoint> pointlist={};
	for (int j=0;j<height;++j) {
			for (int i=0;i<width;++i)  {
				if (getelevation(Mappoint(i,j)) == elevation )
					pointlist.push_back(Mappoint(i,j));
			}
	}
	return pointlist;
}

void Map::print_dijkstra() {
	std::cout<<"Map width: " <<+width<<" height "<<+height<<'\n';
	std::cout<<"Starting point: " <<+start.first<<','<<+start.second;
	std::cout<<"   Ending point: " <<+end.first<<','<<+end.second<<"\n\n";
	for (int j=0;j<height;++j) {
		for (int i=0;i<width;++i)  
			printf("%04i ", getdistance(Mappoint(i,j)) );
		std::cout<<'\n';
	}
}


Map::Map(const char* filename) {
	// read map from file
	std::ifstream mapfile; 
	mapfile.open(filename);
	std::string line;
	while (std::getline(mapfile, line)) 
		mapbuffer.push_back(line);
	height=mapbuffer.size(); 
	width=mapbuffer[0].size(); // all lines have the same width

	// initialize Dijkstra buffer with the default value
	std::vector<int16_t>(tempvector);
	for (int i=0; i<width; ++i)
		tempvector.push_back(max_d);
	for (int j=0; j<height; ++j)
		disbuffer.push_back(tempvector);



	char c;
	// set start and end points, initialize Dijkstra value
	for (int16_t i=0;i<width;++i) {
		for (int16_t j=0;j<height;++j) {
			c=getelevation(Mappoint(i,j));
			if (c=='S') {
				setelevation(Mappoint(i,j),'a');
				start.first=i;
				start.second=j;
			}
			if (c=='E') {
				setelevation(Mappoint(i,j),'z');
				setdistance(Mappoint(i,j),0);
				end.first=i;
				end.second=j;
			}
		}
	}	
}
