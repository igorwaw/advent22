#!/usr/bin/python3

import pygame

# constants
INPUTFILE="9-small.txt"
WIDTH=1000
HEIGHT=600

#global variables
moves=[]

def read_file(filename):
    global moves
    with open(filename) as inputfile:
        for line in inputfile:
            direction,steps=line.rstrip().split()
            moves.append([direction,int(steps)])


# initialize pygame
pygame.init()
screen=pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
running=True


read_file(INPUTFILE)
print(moves)

# main event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False

    # Fill the background with black
    screen.fill((0, 0, 0))
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # Flip the display
    pygame.display.flip()
    clock.tick(30) # wait here to ensure 30FPS

#end event loop, cleanup here
pygame.quit()
