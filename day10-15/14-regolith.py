#!/usr/bin/python3

# This one does both parts


FILENAME="14-input.txt"

STARTSAND=(500,0)

STATITERATIONS=100000 # how often to print stats
MAXITERATIONS=10000000
printmap=True # print part of map at the end

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
                    x1, y1 = onerockline[i].split(',')
                    x2, y2 = onerockline[i+1].split(',')
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

# for part 2
max_sand_height2=max_sand_height+2 # max height2
rocks.update( { (x,max_sand_height2) for x in range(1000)  } ) # add layer of rock at the bottom



part1_filled=False
part2_filled=False
sand_count=0
iterations=0

###################  MAIN LOOP ######################


while not part2_filled: # iterate over all sand
    # create new grain
    sand_count+=1
    #print("Grain ",sand_count)
    x,y=STARTSAND
    stopped=False
    while not stopped: #iterate over current grain of sand
        # check number of iterations for stats and safety check
        iterations+=1
        if iterations>MAXITERATIONS:
            print("Max iterations exceeded")
            part2_filled=True
            break
        if iterations%STATITERATIONS==0:
            print(f"At iteration {iterations}, number of grains {sand_count}")
        # check the grain
        prev_x, prev_y = x,y
        y+=1
        if (not part1_filled) and (y>max_sand_height):
            answer_part1=sand_count-1 # the last grain overflowed
            #print ("found answer for part 1: ", answer_part1)
            part1_filled=True

        stopped=True # assume the path is blocked unless proven otherwise

        for deltax in (0,-1,+1):
            #print (f"  trying {x+deltax},{y}")
            if ((x+deltax,y) not in rocks) and ((x+deltax,y) not in sand): # found clear path
                x+=deltax
                stopped=False
                break;
        if (stopped):
            #print(f"   stopped at {prev_x},{prev_y}")
            sand.add((prev_x,prev_y))
    if STARTSAND in sand: # starting point is blocked
        answer_part2=sand_count
        part2_filled=True


############# REGOLITH: ENDGAME  ##################




if (printmap):
    # print part of map
    for y in range(0,40):
        for x in range(450, 550):
            if (x,y) in rocks: c='█'
            elif (x,y) in sand: c='o'
            else: c='.'
            print(c, end='')
        print()


print('\n')
print("Part 1, grains of sand: ", answer_part1 )
print("Part 2, grains of sand: ", answer_part2 )
