#include "12-map.h"
#include <vector>
#include <algorithm>
#include <memory>
#include <utility>

const char* filename="12-small.txt";


// node in route has location and direction (0-4)
//using routenode = std::pair<Mappoint,int16_t>;

void calculate_dijkstra(std::shared_ptr<Map> map, Mappoint previouspoint, Mappoint nextpoint ) {
	char current_elevation=map->getelevation(previouspoint);
	
	std::cout<<"checking path from "<<previouspoint<<" to "<<nextpoint<<'\n';
	if (nextpoint.x<0 or nextpoint.x>=map->getwidth() or nextpoint.y<0 or nextpoint.y>=map->getheight()) {// out of map, skip that direction
		std::cout<<"    "<<nextpoint<<" is out of map, skipping\n";
		return;
	}
	char nextelevation=map->getelevation(nextpoint);
	if (nextelevation-1 > current_elevation) {
		std::cout<<"    new elevation"<<nextelevation<<" is too high from current elevation ("<<current_elevation<<"), skipping\n";
		return;
	}
	std::cout<<"    "<<nextpoint<<" elevation "<<nextelevation<<" is possible route \n";
	int16_t newdistance=map->getdistance(previouspoint) + 1;
	map->setdistance(nextpoint, newdistance);
}


int checkpath(std::shared_ptr<Map> map, Mappoint startpoint) {
	int16_t pathlength=-1;
	std::vector<Mappoint> to_check = {};
	to_check.push_back(startpoint);

	int iterations=0;
	while (!to_check.empty()) {
		++iterations;
		std::cout<<"Calculating distance, current iteration: "<<iterations<<'\n';
		if (iterations>2) break;
		Mappoint prevpoint=to_check.back();
		to_check.pop_back();
		for (int i=0; i<4;++i) {
			Mappoint nextpoint=prevpoint;
			switch(i) {
				case 0:  --nextpoint.x; break;
				case 1:  ++nextpoint.x; break;
				case 2:  --nextpoint.y; break;
				case 3:  ++nextpoint.y; break;
			}
			calculate_dijkstra(map, prevpoint, nextpoint);
		 }
	}


	return pathlength;
}



int main() {
	
	std::shared_ptr<Map> map(new Map(filename) );
	map->print(true);
	map->print_dijkstra();
	Mappoint start=map->getstart(); // set start of path
	int shortest=checkpath(map, start);
	map->print_dijkstra();
	if (shortest>0)
		std::cout<<" Found shortest route of length "<<shortest<<"\n\n";
	else
		std::cout<<"Shortest route not found \n\n";
	
	
}
