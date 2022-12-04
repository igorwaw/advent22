#!/usr/bin/python3

INPUTFILE="4-input.txt"


def get_next_pair(filename):
    with open(filename) as inputfile:
        for line in inputfile:
            yield line.strip().split(',')


def make_range(str):
    lower,upper=str.split('-')
    return int(lower),int(upper)


def check_contain(left,right):
    leftmin,leftmax=make_range(left)
    rightmin,rightmax=make_range(right)
    if leftmin>=rightmin and leftmax<=rightmax:  # left contained in right
        return 1
    elif rightmin>=leftmin and rightmax<=leftmax:
        return 1
    else:
        return 0


def check_overlap(left,right):
    leftmin,leftmax=make_range(left)
    rightmin,rightmax=make_range(right)
#    if leftmax>=rightmin and leftmin<=rightmax:
    if leftmin<=rightmin and leftmax>=rightmin:
        return 1
    elif rightmax>=leftmin and rightmin<=leftmin:
        return 1
    else:
        return 0


elfcount=0
contcount=0
overlapcount=0
for leftpack,rightpack in get_next_pair(INPUTFILE):
    elfcount+=1
    contain=check_contain(leftpack,rightpack)
    overlap=check_overlap(leftpack,rightpack)
    contcount+=contain
    overlapcount+=overlap
    print("Elf:", elfcount, "left:", leftpack, "right:", rightpack, "is contained: ", contain, "is overlapping: ", overlap)

print("--------------------------")
print("Number of elves: ", elfcount, "total contains: ", contcount, "overlaps: ", overlapcount)
