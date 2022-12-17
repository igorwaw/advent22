#include "12-map.h"
#include <vector>
#include <algorithm>
#include <memory>
#include <utility>
#include <queue>
#include <set>

const char* filename="12-input.txt";
const int maxiterations=10000;

// point in Dijkstra queue has coords and distance from start
// define here datatype and comparator for the priority queue
using Dijspoint = std::pair<Mappoint,int16_t>; 
class Compare {
	public:
		bool operator()(const Dijspoint& lhs, const Dijspoint& rhs) {
			return lhs.second > rhs.second;
	}
};



int checkpath(std::shared_ptr<Map> map, Mappoint startpoint) {
	std::set<Mappoint> visited = {};
	std::priority_queue<Dijspoint, std::vector<Dijspoint>, Compare> to_check = {};
	std::set<Mappoint> to_check2 = {}; // priority queue doesn't support search, this set is used to protect from adding same element twice
	to_check.emplace(startpoint,0);
	to_check2.insert(startpoint);

	int iterations=0;
	while (!to_check.empty()) {
		++iterations;
		std::cout<<"Calculating distance, current iteration: "<<iterations<<'\n';
		if (iterations>maxiterations) break;
		Dijspoint currentdijspoint=to_check.top();
		to_check.pop();
		Mappoint currentpoint=currentdijspoint.first;
		int16_t currentdistancec=currentdijspoint.second;
		to_check2.erase(currentpoint);
		visited.insert(currentpoint);

		if (currentpoint==map->getend()) {
			int16_t distance=map->getdistance(currentpoint);
			std::cout<<"FOUND ROUTE TO THE END - LENGTH "<<distance<<"\n";
			//return distance;
		}
		for (int i=0; i<4;++i) {
			Mappoint nextpoint=currentpoint;
			switch(i) {
				case 0:  --nextpoint.first; break;
				case 1:  ++nextpoint.first; break;
				case 2:  --nextpoint.second; break;
				case 3:  ++nextpoint.second; break;
			}
			char current_elevation=map->getelevation(currentpoint);
	
			std::cout<<"checking path from "<<currentpoint.first<<','<<currentpoint.second<<" to "<<nextpoint.first<<','<<nextpoint.second<<'\n';
			if (nextpoint.first<0 or nextpoint.first>=map->getwidth() or nextpoint.second<0 or nextpoint.second>=map->getheight()) {// out of map, skip that direction
				std::cout<<"    "<<nextpoint.first<<','<<nextpoint.second<<" is out of map, skipping\n";
				continue;
			}
			char nextelevation=map->getelevation(nextpoint);
			if (nextelevation-1 > current_elevation) {
				std::cout<<"    new elevation ("<<nextelevation<<") is too high from current elevation ("<<current_elevation<<"), skipping\n";
				continue;
			}
			//if( std::find(visited.begin(), visited.end(), nextpoint) != visited.end() ) {
			if( visited.count(nextpoint) ) {
				std::cout<<"    "<<nextpoint.first<<','<<nextpoint.second<<" already visited, skipping\n";
				continue;
			}
			std::cout<<"    "<<nextpoint.first<<','<<nextpoint.second<<" elevation "<<nextelevation<<" is possible route \n";
			int16_t newdistance=map->getdistance(currentpoint) + 1;
			if ( newdistance < map->getdistance(nextpoint) ) { // new distance is shorter than the old distance, update
				map->setdistance(nextpoint, newdistance);
				if( !to_check2.count(nextpoint) ) {
					to_check.emplace(nextpoint, newdistance);
					to_check2.insert(nextpoint);
				}
			}
		 }
	}


	return map->getdistance(map->getend());
}



int main() {
	
	std::shared_ptr<Map> map(new Map(filename) );
	map->print(true);
	map->print_dijkstra();
	Mappoint start=map->getstart(); // set start of path

	auto shortest=checkpath(map, start);
	map->print_dijkstra();
	if (shortest<max_d)
		std::cout<<" Found shortest route of length "<<shortest<<"\n\n";
	else
		std::cout<<"Shortest route not found \n\n";
	
	
}
