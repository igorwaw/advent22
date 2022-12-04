#!/usr/bin/python3

INPUTFILE="3-input.txt"


def get_next_pair(filename):
    with open(filename) as inputfile:
        for line in inputfile:
            n = len(line)
            leftpart = line[0:n//2]
            rightpart = line[n//2:]
            yield leftpart,rightpart
        

elfcount=0
for leftpack,rightpack in get_next_pair(INPUTFILE):
    elfcount+=1
    leftset=set(leftpack)
    rightset=set(rightpack)
    print("Elf:", elfcount, "left:", leftset, "right:", rightset)