#!/usr/bin/python3

INPUTFILE="3-input.txt"


def get_next_pair(filename):
    with open(filename) as inputfile:
        for line in inputfile:
            n = len(line)
            leftpart = line[0:n//2]
            rightpart = line[n//2:]
            yield leftpart,rightpart
        


def calculate_priority(item):
    if 'a'<=item<='z':
        return ord(item)-ord('a')+1
    else:
        return ord(item)-ord('A')+27



    

elfcount=0
priosum=0
for leftpack,rightpack in get_next_pair(INPUTFILE):
    elfcount+=1
    leftset=set(leftpack)
    rightset=set(rightpack)
    commonset = leftset & rightset
    commonchar=next(iter(commonset)) # ugly way to extract element from 1-element set
    priority=calculate_priority(commonchar)
    priosum+=priority
    print("Elf:", elfcount, "left:", leftset, "right:", rightset, "common: ", commonchar, "priority: ", priority)

print("--------------------------")
print("Number of elves: ", elfcount, "Total prio: ", priosum)
