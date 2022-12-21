#!/usr/bin/python3

from collections import defaultdict

FILENAME="14-small.txt"

STARTSAND=(500,0)


###################  FUNCTIONS ######################


def read_input() -> set( (int,int) ):
    """ parses input file, returns set of coordinates for rocks """
    with open(FILENAME) as inputfile:
        newrocks=set()
        for line in inputfile:
            onerockline=line.strip().split(" -> ")
            i=0
            while True:
                try:
                    x1, y1=onerockline[i].split(',')
                    x2, y2  =onerockline[i+1].split(',')
                except IndexError:
                    break;
                i+=1
                x1,y1,x2,y2=map(int, [x1,y1,x2,y2] )
                xrange  = range( min(x1,x2), max(x1,x2)+1  )
                yrange  = range( min(y1,y2), max(y1,y2)+1  )
                newrocks.update( { (x,y) for x in xrange for y in yrange  } )
    return newrocks









################ INITIALIZATION #############



rocks=read_input()
print(rocks)

# calculate max height of sand before it starts dropping into the abyss
# equals to the vertical position of the lowest rock
max_sand_height=max( (y for _,y in rocks) )
#print ("max sand height: ", max_sand_height)



###################  MAIN LOOP ######################
#while running:




############# REGOLITH: ENDGAME  ##################


#print("Grains of sand: ", get_sand_count() )