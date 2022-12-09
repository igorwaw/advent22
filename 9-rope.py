#!/usr/bin/python3

import pygame

# constants
#INPUTFILE="9-small.txt"
INPUTFILE="9-input.txt"
WIDTH=1500
HEIGHT=900
ELSIZE=5 # size of the element on the screen
FPS=10000 # how many animation frames / calculation steps per second
NUMKNOTS=2

# colors for current/old position of tail (red) and head (blue)
color={ 'T': (255,0,0), 'oldT': (100,50,50), 'H': (0,0,255), 'oldH': (50,50,100) }

#global variables
moves=[] # sequence of moves read from the input file
visited=set() # stores coordinates of tail positions - assume start point is 0,0



########## FUNCTIONS - TASK RELATED ################

# read moves from the input file
def read_file(filename):
    global moves
    with open(filename) as inputfile:
        for line in inputfile:
            direction,steps=line.rstrip().split()
            moves.append([direction,int(steps)])
    moves.reverse() # so we can use it as stack

def head_next_position(head_x, head_y):
    if len(moves)==0: # end of moves, stay in place
        return head_x, head_y
    #print(moves[-1]) # debug
    direction,steps=moves[-1]
    if steps==1:
        moves.pop()
    else:
        moves[-1][1]-=1  # that looks ugly! decrement number of steps in the last elment of the moves list
    if direction=="R":
        new_x=head_x+1
        new_y=head_y
    elif direction=="L":
        new_x=head_x-1
        new_y=head_y
    elif direction=="D":
        new_x=head_x
        new_y=head_y-1
    elif direction=="U":
        new_x=head_x
        new_y=head_y+1    
    return new_x, new_y

def tail_next_position(tail_x, tail_y, head_x, head_y):
    deltax=tail_x-head_x
    deltay=tail_y-head_y
    new_x, new_y = tail_x, tail_y # starting point: old position
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

################### MAIN LOOP  #############
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False

    draw_element("oldH", head_x, head_y)
    draw_element("oldT", tail_x, tail_y)
    head_x, head_y = head_next_position(head_x, head_y)
    draw_element("H", head_x, head_y)
    for i in range(1,NUMKNOTS):
        tail_x, tail_y = tail_next_position(tail_x, tail_y, head_x, head_y)
        draw_element("T", tail_x, tail_y)
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
