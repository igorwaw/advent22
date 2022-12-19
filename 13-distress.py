#!/usr/bin/python3

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
        

#@dataclass
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
                self.left.append(eval(newline.strip()))
                # not checking if the next line exists
                self.right.append(eval(inputfile.readline().strip()))
                inputfile.readline()
    

    def print(self):
        for i in range(len(self.left)):
            print(f"{i+1} Left: {self.left[i]}   right: {self.right[i]}")


    def rightorder(self, index: int) ->bool:
        leftval=self.left[index-1]
        rightval=self.right[index-1]
        if defdebug: print(f"{index} Left: {leftval}   right: {rightval}")
        if listcompare(leftval, rightval)<0:
            return True
        else:
            return False
        






smallsignal=Signal("13-small.txt")
#smallsignal.print()
sumindices=0
for i in range(1,smallsignal.count+1):
    isright=smallsignal.rightorder(i)
    if (isright):
        sumindices+=i
        if defdebug: print(f"Message {i} in the right order\n")
    else:
        if defdebug: print(f"Message {i} in the wrong order\n")
print("\n\nPart 1, sum of indices: ",sumindices)


bigsignal=Signal("13-input.txt")
sumindices=0
for i in range(1,bigsignal.count+1):
    isright=bigsignal.rightorder(i)
    if (isright):
        sumindices+=i
        if defdebug: print(f"Message {i} in the right order\n")
    else:
        if defdebug: print(f"Message {i} in the wrong order\n")
print("\n\nPart 2, sum of indices: ",sumindices)
