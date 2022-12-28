#!/usr/bin/python3

from collections import defaultdict
import pygame
from mappoint import Mappoint, PointWithDistance
from queue import PriorityQueue

# this one only does part 2

FILENAME="14-input.txt"
# size of cave
WIDTH=1000
HEIGHT=250
ELSIZE=30 # font size


STARTSAND=Mappoint(500,0)

# special values for cave map
MAXPATH=888 # unexplored space
ROCK=999



# for visualization
UPDATE_ITER=1000

colormap=defaultdict(lambda : (20,20,200)) # sets default color
colormap[MAXPATH]=(0,0,0)
colormap[ROCK]=(255,0,0) 



###################  FUNCTIONS ######################

def get_sand_count() ->int:
    """ counts grains of sand, defined as: every point that's neither empty space nor rock """
    global cavemap
    count=0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if cavemap[y][x] <MAXPATH:
                count+=1
    return count



def write_below(message):
    global font, screen
    """ prints a message at the bottom of the window """
    text = font.render(message, True, (200,200,200), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT-(ELSIZE))
    screen.blit(text, textRect)

def draw_screen():
    """ redraws map of cave """
    global screen, cavemap
    for x in range(WIDTH):
        for y in range(HEIGHT):
            pixelvalue=colormap[ cavemap[y][x] ]
            screen.set_at((x,y),  pixelvalue)


def read_input() -> list:
    """ parses input file, returns list of coordinates for rocks """
    with open(FILENAME) as inputfile:
        newrocks=[]
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
                newrocks.append( map(int, [ x1, y1, x2, y2]) )
            #print(onerockline)
    return newrocks


def add_rock(rock):
    """ adds new piece of rock to the cavemap """
    global cavemap
    x1,y1,x2,y2 = rock
    start_x=min(x1,x2)
    start_y=min(y1,y2)
    end_x=max(x1,x2)
    end_y=max(y1,y2)
    #print(f"adding rock from {start_x},{start_y} to {end_x},{end_y}")
    for x in range(start_x,end_x+1):
        for y in range(start_y,end_y+1):
            cavemap[y][x]=ROCK    



def get_sand_height():
    """ calculate max height of sand before it starts dropping into the abyss
        equals to vertical distance between starting point and the lowest rock """
    # find the lowest rock - searching from the bottom
    for y in range(HEIGHT-1,0,-1):
        try:
            cavemap[y].index(ROCK)
        except ValueError: # not found, try next row
            continue
        return y-STARTSAND.y # no exception, found it:
    return 0 # not found


def add_next_step(new_x: int, new_y: int, newdistance: int):
    """ adds next point to check to the queue, only used by findpath_step() """
    global to_check,cavemap
    newpoint=Mappoint(new_x, new_y)
    # normally we should check if new distance is smaller than old but in this case we can
    # only reach every point once
    cavemap[new_y][new_x]=newdistance 
    #print(f"next point to check: {new_x},{new_y} distance {newdistance}")
    to_check.put(PointWithDistance(newdistance,newpoint))
    


def findpath_step():
    """ does one step of Dijkstra algorithm  """
    global to_check,cavemap, part2done
    if to_check.empty():
        #raise IndexError("no more points to check")
        part2done=True
        return
    currentpoint=to_check.get()
    #visited.add(currentpoint.point)
    #print("Checking ",currentpoint)
    
    # check if we are in the abyss
    #if currentpoint.distance>max_sand_height:
    #    part1done=True
    # check point below

    new_x=currentpoint.point.x
    new_y=currentpoint.point.y+1
    for deltax in (-1,0,1):
        if cavemap[new_y][new_x+deltax]==MAXPATH:
            add_next_step(new_x+deltax, new_y, currentpoint.distance+1)
    


################ INITIALIZATION #############


# initialize pygame
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Regolith Reservoir')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
screen.fill((0, 0, 0)) # Fill the background with black
running=True


# initialize the rest
cavemap= [[MAXPATH for i in range(WIDTH)] for j in range(HEIGHT)]
#visited=set()
to_check=PriorityQueue()
to_check.put( PointWithDistance(0,STARTSAND) )
part2done=False

rocks=read_input()
#print(rocks)
for rock in rocks:
    add_rock(rock)

max_sand_height=get_sand_height()
print ("max sand height: ", max_sand_height)

# add layer of rocks at the bottom
add_rock( (0,max_sand_height+2, WIDTH-1, max_sand_height+2) )


###################  MAIN LOOP ######################
counter=0
part2done=False
onemoreupdateneeded=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False

    if not part2done:
        findpath_step() # do one step of simulation
    
    if part2done and onemoreupdateneeded:  # redraw screen one more time
        print("here")
        onemoreupdateneeded=False
        draw_screen()
        grains=1+get_sand_count()
        write_below(f"Answer found: Sand count: {grains}")
        pygame.display.flip()

    if counter%UPDATE_ITER==0 and not part2done:
        draw_screen()
        grains=get_sand_count()
        write_below(f"Current sand count: {grains}")
        pygame.display.flip()
    #clock.tick(FPS) # wait here
    counter+=1

############# REGOLITH: ENDGAME  ##################
pygame.quit()

## check map fragment for debugging
for y in range(0,11):
    for x in range(490,510):
        if cavemap[y][x]==MAXPATH:
            print("...", end=' ')
        elif cavemap[y][x]==ROCK:
            print("███", end=' ')
        else:
            print(f"{cavemap[y][x]:03d}", end=' ')
    print()

print("Grains of sand: ", grains )