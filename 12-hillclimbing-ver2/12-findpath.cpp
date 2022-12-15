#include "12-map.h"
#include <vector>
#include <algorithm>
#include <memory>
#include <utility>

const char* filename="12-small.txt";
const int16_t max_level=35; // maximum tree depth

// node in route has location and direction (0-4)
enum DIRECTION {notchecked, top, bottom, left, right};
using routenode = std::pair<Mappoint,int16_t>;

int checkpath(std::shared_ptr<Map> map, Mappoint startnode) {
	std::vector<Mappoint> visited {}; // list of visited nodes
	std::vector<routenode> to_check {};
	
	visited.push_back(startnode);
	to_check.emplace_back(startnode, notchecked); 
	
	while (! to_check.empty() ) {
		routenode current_node=to_check.back();
		to_check.pop_back();
		if (current_node.second==right) // all directions from this node were already checked
			continue;
		++current_node.second;
		char current_elevation=map->getelevation(current_node.first);
		std::cout<<"checking "<<current_node.first<<" elevation "<<current_elevation<<" direction "<<current_node.second<<'\n';
	}
	return -1; // route not found
	
	
	
	
	/*
	for (int i=0; i<4;++i) {
		if (currentnode->child[i]!=nullptr) // already checked
			continue;
		int16_t x=p.x;
		int16_t y=p.y;
		switch (i) {
			case top: --y; break;
			case bottom: ++y; break;
			case left: --x; break;
			case right: ++x; break;
		}
		Mappoint newpoint( x,y );
		if (x<0 or x>=map->getwidth() or y<0 or y>=map->getheight()) {// out of map, skip that direction
			//std::cout<<"    "<<newpoint<<" is out of map, skipping\n";
			continue;
		}
		
		if( std::find(visited.begin(), visited.end(), newpoint) != visited.end() ) { // that point was already visited, skip that direction
			//std::cout<<"    "<<newpoint<<" already visited, skipping\n";
			continue;
		}
		char newh=map->getpoint(newpoint);
		//if (!newh)
		//	throw std::runtime_error("no elevation\n");
		if ( newh-1 > current_elevation )  {// too high, skip that direction
			//std::cout<<"    "<<newpoint<<" is too high ("<<newh<<"), skipping\n";
			continue;
		}
		currentnode->addchild((DIRECTION)i); // direction OK, create new node
		if ( newpoint==map->getend() ) { // end point reached, returning
			routefound=true;
			int16_t routelength=currentnode->getdepth()+1;
			if (routelength < shortest ) 
				shortest=routelength;
			std::cout<<"\n-------------  Reached end, route length "<<routelength<<" --------\n";
			return;
		}
		else
			checkpath( maxlevel, map, currentnode->child[i], visited); // recursively check new node
	}
	*/
	
}



int main() {
	
	std::shared_ptr<Map> map(new Map(filename) );
	map->print(true);
	
	Mappoint start=map->getstart(); // set start of path
	int shortest=checkpath(map, start);
	
	if (shortest>0)
		std::cout<<" Found shortest route of length "<<shortest<<"\n\n";
	else
		std::cout<<"Shortest route not found, max length of "<<max_level<<" reached\n\n";
	
	
}
