#!/usr/bin/python3

INPUTFILE="4-input.txt"


def get_next_pair(filename):
    with open(filename) as inputfile:
        for line in inputfile:
            yield line.split(',')


def check_contain(left,right):
    return 0


elfcount=0
contcount=0
for leftpack,rightpack in get_next_pair(INPUTFILE):
    elfcount+=1
    contain=check_contain(leftpack,rightpack)
    contcount+=contain
    print("Elf:", elfcount, "left:", leftpack, "right:", rightpack, "is contained: ", contain)

print("--------------------------")
print("Number of elves: ", elfcount, "Number of total contain: ", contcount)
