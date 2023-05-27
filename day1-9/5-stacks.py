#!/usr/bin/python3

INPUTFILE="5-input.txt"
NUMSTACKS=9

stacks=[]
moves=[]

def readfile(filename):
    doing_moves=False
    with open(filename) as inputfile:
        for line in inputfile:
            if line.strip()=='':
                doing_moves=True
                continue
            if doing_moves:
                read_moves(line.rstrip())
            else:
                read_stacks(line.rstrip())


def read_moves(line):
    #print("Do moves: ",line)
    global moves
    _,num,_,stack_from,_,stack_to=line.split()
    moves.append([int(num),int(stack_from)-1,int(stack_to)-1])


def read_stacks(line):
        if '1' in line:
            return
        #print("Do stacks: ",line)
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
        #print ("Moving ",num,"elements from", stacks[stack_from], "to", stacks[stack_to] )
        for _ in range(num):
            stacks[stack_to].append( stacks[stack_from].pop() )


def do_moves_v2():
    for move in moves:
        num,stack_from,stack_to=move
        tempstack=[]
        #print ("Moving ",num,"elements from", stacks[stack_from], "to", stacks[stack_to] )
        for _ in range(num):
            element=stacks[stack_from].pop()
            tempstack.append(element)
        tempstack.reverse()
        for e in tempstack:
            stacks[stack_to].append(e)


        
def give_answer():
    answer=""
    for i in range(NUMSTACKS):
        answer+=stacks[i].pop() 
    return answer



# part 1
stacks=[ [] for _ in range(NUMSTACKS) ]
readfile(INPUTFILE)
do_moves_v1()
print("Part 1: ", give_answer())

# part 2
# clear data and read file again
stacks.clear()
stacks=[ [] for _ in range(NUMSTACKS) ]
moves.clear()
readfile(INPUTFILE)

do_moves_v2()
print("Part 2: ", give_answer())

