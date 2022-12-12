#!/usr/bin/python3

import heapq

INPUTFILE="1-input.txt"

elves=[]

with open(INPUTFILE) as inputfile:
	elf=0
	for line in inputfile:
		if line in ['\n','\r\n']:
			elves.append(elf)
			elf=0
		else:
			elf=elf+int(line)

print ("Number of elves ", len(elves))

print ("Most calories 1", sum(heapq.nlargest(1, elves)))
print ("Most calories 3", sum(heapq.nlargest(3, elves)))
