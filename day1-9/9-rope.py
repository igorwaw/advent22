#!/usr/bin/python3

import pygame

# constants
#INPUTFILE="9-medium.txt"
INPUTFILE="9-input.txt"
WIDTH=1500
HEIGHT=900
ELSIZE=5 # size of the element on the screen
FPS=5000 # how many animation frames / calculation steps per second
NUMKNOTS=10 # number of knots, including head and tail

# colors for current/old position of tail (red), head (blue), middle (purple)
color={ 'T': (255,0,0), 'oldT': (100,50,50), 'H': (0,0,255), 'oldH': (50,50,100), 'M': (100,50,100), 'oldM': (100,50,100) }

#global variables
moves=[] # sequence of moves read from the input file
visited=set() # stores coordinates of tail positions
prev_knot=[]

########## FUNCTIONS - TASK RELATED ################

# read moves from the input file
def read_file(filename):
    global moves
    with open(filename) as inputfile:
        for line in inputfile:
            direction,steps=line.rstrip().split()
            moves.append([direction,int(steps)])
    moves.reverse() # so we can use it as a stack

def head_next_position(head_x, head_y):
    new_x, new_y = head_x, head_y # starting point for calculations: old position
    if len(moves)!=0: # when there are no moves, stay in place
        direction,steps=moves[-1]
        if steps==1:
            moves.pop()
        else:
            moves[-1][1]-=1  # that looks ugly! decrement number of steps in the last element of the moves list
        if direction=="R":
            new_x+=1
        elif direction=="L":
            new_x-=1
        elif direction=="D":
            new_y-=1
        elif direction=="U":
            new_y+=1    
    return new_x, new_y

def tail_next_position(tail_x, tail_y, head_x, head_y):
    deltax=tail_x-head_x
    deltay=tail_y-head_y
    new_x, new_y = tail_x, tail_y # starting point for calculations: old position
    if abs(deltax)<=1 and abs(deltay)<=1: # distance 0 or 1, nothing to do
        pass
    elif deltax==0: # same column, different row
        if deltay>=2:
            new_y-=1
        elif deltay<=-2:
            new_y+=1
    elif deltay==0: # same row, different column
        if deltax>=2:
            new_x-=1
        elif deltax<=-2:
            new_x+=1
    else: # different row and column
        if deltay>=1:
            new_y-=1
        else:
            new_y+=1
        if deltax>=1:
            new_x-=1
        else:
            new_x+=1
    return new_x, new_y

########## FUNCTIONS - VISUALIZATION ################

# draws element on screen, takes LOGICAL coordinates: (0,0) is the center
def draw_element(type, x, y):
    # calculate pixel coordinates
    screen_x=(WIDTH//2)+x*ELSIZE
    screen_y=(HEIGHT//2)+y*ELSIZE
    pygame.draw.circle(screen, color[type], (screen_x, screen_y), ELSIZE)



# prints a message at the bottom of the window
def write_below(message):
    text = font.render(message, True, (200,200,200), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT-(ELSIZE*4))
    screen.blit(text, textRect)


################### INITIALIZATION  #############


# initialize pygame
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rope Bridge')
clock = pygame.time.Clock()
font = pygame.font.Font(None, ELSIZE*3)
screen.fill((0, 0, 0)) # Fill the background with black
running=True

# initialize rope
head_x=0
head_y=0
tail_x=0
tail_y=0
read_file(INPUTFILE)
for i in range(0,NUMKNOTS):
    prev_knot.append((0,0))

################### MAIN LOOP  #############
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False

    #we still have old positions, last chance to draw them
    draw_element("oldH", head_x, head_y)
    draw_element("oldT", tail_x, tail_y)
    # calculate and draw head
    head_x, head_y = head_next_position(head_x, head_y)
    draw_element("H", head_x, head_y)

    # calculate further knots, first one should be relative to head
    # all others relative to previous knot
    
    prev_knot[0]=head_x,head_y
    for i in range(1,NUMKNOTS):
        tail_x, tail_y = tail_next_position(prev_knot[i][0], prev_knot[i][1], prev_knot[i-1][0], prev_knot[i-1][1])
        prev_knot[i]=(tail_x,tail_y)
        if i==NUMKNOTS-1:
            draw_element("T", tail_x, tail_y)
        else:
            draw_element("M", tail_x, tail_y)
    visited.add((tail_x, tail_y)) # we can just add the position, set will only store new values
    numvisited=str(len(visited))
    write_below("Tail positions: "+numvisited)

    # Flip the display
    pygame.display.flip()
    clock.tick(FPS) # wait here 

#end event loop, cleanup here
print("Tail positions: "+numvisited)
#print(visited)
pygame.quit()
