#include "12-pathnode.h"
#include "12-map.h"
#include <vector>
#include <algorithm>

const char* filename="12-input.txt";
const int16_t max_level=35; // maximum tree depth
int16_t shortest=max_level;
bool routefound=false;

void checkpath(int16_t maxlevel, std::shared_ptr<Map> map, std::shared_ptr<Pathnode> currentnode, std::vector<Mappoint> visited) {
	if (currentnode->getdepth() == maxlevel) // maximum recusion reached
		return;
		
	Mappoint p=currentnode->getcoords();
	char current_elevation=map->getpoint(p);
	visited.push_back(p); 
	//std::cout<<"checking "<<p<<" elevation "<<current_elevation<<'\n';
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
}



int main() {
	
	std::shared_ptr<Map> map(new Map(filename) );
	map->print(true);
	
	Mappoint start=map->getstart();
	// set start of path
	std::shared_ptr<Pathnode> startpoint( new Pathnode( start ) );
	// create marker for blocked path
	//std::shared_ptr<Pathnode> blocked( new Pathnode( start, 'B' ) );
	
	checkpath(max_level, map, startpoint, std::vector<Mappoint> {});
	
	if (routefound) {
		std::cout<<"####################################\n\n";
		std::cout<<" Found shortest route of length "<<shortest<<"\n\n";
	}
	else
		std::cout<<"Shortest route not found, max length of "<<max_level<<" reached\n\n";
	//startpoint->printtree();
	
	
}
