#!/usr/bin/python3


import sys

# constants

INPUTFILE="10-input.txt"
#INPUTFILE="10-small.txt"
FIRSTCYCLE=20
NEXTCYCLE=40
SCREENWIDTH=40
SCREENHEIGHT=6



def get_strength(cycle,register):
    if (cycle==FIRSTCYCLE) or ((cycle-FIRSTCYCLE)%NEXTCYCLE==0):
            strength=cycle*register
            #print(f"Cycle {n} current signal strength {strength}")
            return strength
    else:
        return 0

def drawpixel(cycle,register):
    global pixelbuf
    row=(cycle-1)//SCREENWIDTH
    col=(cycle-row*SCREENWIDTH)-1
    sprite=range(register-1,register+2)
    try:
        if col in sprite:
            pixelbuf[row][col]='█'
            #print(f"cycle {cycle}: drawing pixel at {row}x{col} sprite position {sprite}")
        #else:
            #print(f"cycle {cycle}: NOT drawing pixel at {row}x{col} sprite position {sprite}")
    except IndexError:
        print("PIXEL POSITON OUT OF RANGE: ",row,col)
        sys.exit(1)


n=0
regX=1
sumstrength=0
pixelbuf=[]
for i in range(0,SCREENHEIGHT):
    pixelbuf.append(list(SCREENWIDTH*' '))

with open(INPUTFILE) as inputfile:
    for line in inputfile:
        line=line.rstrip()
        n+=1
        drawpixel(n,regX)
        sumstrength+=get_strength(n,regX)
        if line=="noop":
            pass
            #print(f"{n} noop")
        elif line[0:4]=="addx":
            value=int(line[5:])
            #print(f"{n} addx {value} register before {regX} after {regX+value}")
            n+=1 # addx takes 2 cycles
            sumstrength+=get_strength(n,regX) # cycle count increased, need to check if it's interesting again
            drawpixel(n,regX)             # addx took 2 cycles, so we need to draw 2 pixels
            regX+=value
        else:
            print("Unknown command", line)
print("\n--------- THE END -----------------")
print(f"Cycle {n} sum {sumstrength}")

for i in range(0,SCREENHEIGHT):
    print(''.join(pixelbuf[i]))
