#!/usr/bin/python3

from functools import cmp_to_key

filename="13-input.txt"
defdebug=False


packet1=[[2]]
packet2=[[6]]



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
    # one integer, one list
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
        
## MAIN

message=[]
       
with open(filename) as inputfile:
    for line in inputfile:
        line=line.strip()
        if line=="": continue
        message.append(eval(line))


message.append(packet1)
message.append(packet2)


message.sort(key=cmp_to_key(listcompare))

#for m in message:    
#    print(m)

pos1=message.index(packet1)+1
pos2=message.index(packet2)+1

print("Decoded key: ", pos1*pos2)
