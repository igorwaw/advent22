#include "12-pathnode.h"


void Pathnode::print() {
    std::cout<<"Node at "<<+coords.x<<','<<+coords.y<<" depth in the tree "<<+depth<<'\n';
}


void Pathnode::addchild(DIRECTION dir) {
	Mappoint newcoords=coords;
	int16_t newdepth=this->depth+1;
	switch(dir) {
		case left:    --newcoords.x; break;
		case right:   ++newcoords.x; break;
		case top:     --newcoords.y; break;
		case bottom:  ++newcoords.y; break;
	}
	this->child[dir]=std::unique_ptr<Pathnode>( new Pathnode(newcoords,newdepth) );
}

void Pathnode::printtree() {
    print();
    for (int i=0; i<4;++i)
		if (child[i]!=nullptr)
			child[i]->printtree();
}

