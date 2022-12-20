#!/usr/bin/python3

INPUTFILE="3-input.txt"


def get_next_pair(filename):
    with open(filename) as inputfile:
        for line in inputfile:
            n = len(line)
            leftpart = line[0:n//2]
            rightpart = line[n//2:]
            yield set(leftpart),set(rightpart)
        

def get_next_group(filename, length):
    with open(filename) as inputfile:
        while True:
            group = []
            for i in range(length):
                try:
                    group.append(set(next(inputfile).strip()))
                except StopIteration:
                    return
                if not group:
                    return
            yield group


def calculate_priority(item):
    if 'a'<=item<='z':
        return ord(item)-ord('a')+1
    else:
        return ord(item)-ord('A')+27



    
#part 1
elfcount=0
priosum=0
for leftset,rightset in get_next_pair(INPUTFILE):
    elfcount+=1
    commonset = leftset & rightset
    commonchar=next(iter(commonset)) # ugly way to extract element from 1-element set
    priority=calculate_priority(commonchar)
    priosum+=priority
    #print("Elf:", elfcount, "left:", leftset, "right:", rightset, "common: ", commonchar, "priority: ", priority)

print("Number of elves: ", elfcount, "Total prio: ", priosum)

groupcount=0
priosum=0

#part 2
for elf1,elf2,elf3 in get_next_group(INPUTFILE,3):
    groupcount+=1
    commonset = elf1 & elf2 & elf3
    commonchar=next(iter(commonset)) # ugly way to extract element from 1-element set
    priority=calculate_priority(commonchar)
    priosum+=priority
    #print("Group:", groupcount, "common: ", commonchar, "priority: ", priority)

print("Number of groups: ", groupcount, "Total prio: ", priosum)
