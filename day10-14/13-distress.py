#!/usr/bin/python3

import ast
from functools import cmp_to_key

filename="13-input.txt"

defdebug=False


# works on ints and (nested) lists of ints
# return -1, 0 or 1
def listcompare(left, right) -> int:
    if defdebug: print(f"   comparing {left} and {right} ")
    # both integers
    if isinstance(left, int) and isinstance(right, int):
        if defdebug: print("   comparing integers")
        if left<right:
            return -1
        elif left>right:
            return 1
        else:
            return 0
    # one integer, one list - pack integer into single-element
    # list and recurse
    if isinstance(left, int) and not isinstance(right, int):
        if defdebug: print("    left integer, right list")
        left=[left]
        return listcompare(left, right)
    if isinstance(right, int) and not isinstance(left, int):
        if defdebug: print("    left list, right integer")
        right=[right]
        return listcompare(left, right)
    # both lists, iterating
    i=0
    while True:
        if defdebug: print("    both lists")
        # check if any list is empty
        leftempty=False
        rightempty=False
        try:
            nextleft=left[i]
        except (IndexError, AttributeError, TypeError) as e: # left list ran out of items first
            if defdebug: print("   left list is empty")
            leftempty=True
        try:
            nextright=right[i]
        except (IndexError, AttributeError, TypeError) as e: # right list ran out of items first
            if defdebug: print("   right list is empty")
            rightempty=True
        i+=1
        if leftempty and rightempty:
            return 0
        if leftempty:
            return -1
        if rightempty:
            return 1
        # no list is empty
        if defdebug: print(f"   in the loop, comparing {nextleft} and {nextright}")
        result=listcompare(nextleft, nextright)
        if result==0: # no decision yet, go to next item
            if defdebug: print (f"   {left} and {right} are equal")
            continue
        else:
            return result
        

class Signal:
    left:  'list[list]'
    right: 'list[list]'
    count: int
    def __init__(self, filename: str):
        self.left=[]
        self.right=[]
        self.count=0
        with open(filename) as inputfile:
            while True:
                newline=inputfile.readline()
                if not newline:
                    break;
                self.count+=1
                self.left.append(ast.literal_eval(newline.strip()))
                # not checking if the next line exists
                self.right.append(ast.literal_eval(inputfile.readline().strip()))
                inputfile.readline()
    

    def print(self):
        for i, (leftval, rightval) in enumerate(zip(self.left,self.right), start=1):
            print(f"{i} Left: {leftval}   right: {rightval}")


    def rightorder(self, index: int) -> bool:
        leftval=self.left[index-1]
        rightval=self.right[index-1]
        if defdebug: print(f"{index} Left: {leftval}   right: {rightval}")
        return listcompare(leftval, rightval) < 0
        




signal=Signal(filename)
sumindices=0
for i in range(1,signal.count+1):
    isright=signal.rightorder(i)
    if (isright):
        sumindices+=i
        if defdebug: print(f"Message {i} in the right order\n")
    else:
        if defdebug: print(f"Message {i} in the wrong order\n")
print("Part 1, sum of indices: ",sumindices)


# part 2 - we need complete data without the left/right division
# plus 2 extra packets
packet1=[[2]]
packet2=[[6]]

message=signal.left+signal.right+[packet1, packet2]
message.sort(key=cmp_to_key(listcompare))
pos1=message.index(packet1)+1
pos2=message.index(packet2)+1


print("Part 2, decoded key: ", pos1*pos2)

