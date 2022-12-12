#!/usr/bin/python3

INPUTFILE="3-input.txt"


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

groupcount=0
priosum=0

for elf1,elf2,elf3 in get_next_group(INPUTFILE,3):
    groupcount+=1
    commonset = elf1 & elf2 & elf3
    commonchar=next(iter(commonset)) # ugly way to extract element from 1-element set
    priority=calculate_priority(commonchar)
    priosum+=priority
    #print("Group:", groupcount, "common: ", commonchar, "priority: ", priority)

print("--------------------------")
print("Number of groups: ", groupcount, "Total prio: ", priosum)
