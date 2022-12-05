#!/usr/bin/python3

import pprint

INPUTFILE="5-input.txt"
NUMSTACKS=9

stacks=[]
moves=[]

def readfile(filename):
    doing_moves=False
    with open(INPUTFILE) as inputfile:
        for line in inputfile:
            if line.strip()=='':
                doing_moves=True
                continue
            if doing_moves:
                read_moves(line.rstrip())
            else:
                read_stacks(line.rstrip())


def read_moves(line):
    print("Do moves: ",line)
    global moves
    _,num,_,stack_from,_,stack_to=line.split()
    moves.append([int(num),int(stack_from)-1,int(stack_to)-1])




def read_stacks(line):
        if '1' in line:
            return
        print("Do stacks: ",line)
        global stacks
        for i in range(1,NUMSTACKS+1):
            try:
                nextchar=line[4*i-3]
                if (nextchar!=' '):
                    stacks[i-1].insert(0,nextchar)
            except:
                pass


def do_moves_v1():
    global stacks
    for move in moves:
        num,stack_from,stack_to=move
        print ("Moving ",num,"elements from", stacks[stack_from], "to", stacks[stack_to] )
        for i in range(0,num):
            element=stacks[stack_from].pop()
            stacks[stack_to].append(element)


def do_moves_v2():
    global stacks
    for move in moves:
        num,stack_from,stack_to=move
        tempstack=[]
        #print ("Moving ",num,"elements from", stacks[stack_from], "to", stacks[stack_to] )
        for i in range(0,num):
            element=stacks[stack_from].pop()
            tempstack.append(element)
        tempstack.reverse()
        for e in tempstack:
            stacks[stack_to].append(e)


        
def give_answer():
    answer=""
    for i in range(0,NUMSTACKS):
        answer+=stacks[i].pop()
    print("The answer is: ", answer)



for i in range(0,NUMSTACKS):
    stacks.append([])
readfile(INPUTFILE)
print("Stacks before")
pprint.pprint(stacks)
#pprint.pprint(moves)
do_moves_v2()
print("Stacks after")
pprint.pprint(stacks)
give_answer()
