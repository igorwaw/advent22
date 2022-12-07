#!/usr/bin/python3


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

elves.sort(reverse=True)
print ("Most calories 1", elves[0])
print ("Most calories 3", elves[0]+elves[1]+elves[2])
