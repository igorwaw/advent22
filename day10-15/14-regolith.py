#!/usr/bin/python3


FILENAME="14-input.txt"

STARTSAND=(500,0)

STATITERATIONS=10000 # how often to print stats

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


rocks: set =read_input()

sand=set()

# calculate max height of sand before it starts dropping into the abyss
# equals to the vertical position of the lowest rock
max_sand_height=max( (y for _,y in rocks) )
print ("max sand height: ", max_sand_height)

notfilled=True
sand_count=0
iterations=0

###################  MAIN LOOP ######################


while notfilled: # iterate over all sand
    # create new grain
    sand_count+=1
    #print("Grain ",sand_count)
    x,y=STARTSAND
    stopped=False
    while not stopped: #iterate over current grain of sand
        # check number of iterations for stats
        iterations+=1
        if iterations%STATITERATIONS==0:
            print(f"At iteration {iterations}, number of grains {sand_count}")
        # check the grain
        prev_x, prev_y = x,y
        y+=1
        if y>max_sand_height:
            notfilled=False
            break
        stopped=True # assume the path is blocked unless proved otherwise
        for deltax in (0,-1,+1):
            #print (f"  trying {x+deltax},{y}")
            if ((x+deltax,y) not in rocks) and ((x+deltax,y) not in sand):
                x+=deltax
                stopped=False
                break;
        if (stopped):
            #print(f"   stopped at {prev_x},{prev_y}")
            sand.add((prev_x,prev_y))


sand_count-=1 # the last grain overflowed

############# REGOLITH: ENDGAME  ##################


print("Grains of sand: ", sand_count )
#print("Rocks: ", rocks )
#print("Sand: ", sand )