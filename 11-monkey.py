#!/usr/bin/python3

from dataclasses import dataclass
from collections.abc import Callable

INPUTFILE="11-input.txt"
NUMROUNDS=20

Operation = Callable[[int], int]

@dataclass
class Monkey:
    count=0 # static, number of monkeys
    number: int
    items: list[int]
    operation: str
    test: str
    truetarget: int
    falsetarget: int
    inspections: int

    def __init__(self):
        Monkey.count+=1
        self.number=Monkey.count-1
        self.items=[]
        self.test=""
        self.truetarget=-1
        self.falsetarget=-1
        self.inspections=0

    def add_item(self, item: int):
        self.items.append(item)

    def add_operation(self, opstring: str):
        self.operation=lambda old: eval(opstring.split("=")[-1])


def readfile():
    global monkeys
    monkey=Monkey()
    with open(INPUTFILE) as inputfile:
        for line in inputfile:
            line=line.strip()
            if "Starting items" in line:
                _,items=line.split(':')
                items2=items.split(',')
                for item in items2:
                    monkey.add_item(int(item))
            elif "Operation" in line: # TODO
                #print ("operation: ", str(line.split("=")[-1]) )
                monkey.add_operation(line)
            elif "Test" in line:
                _,_,_,value=line.split()
                monkey.test=int(value.strip())
            elif "If true" in line:
                target=int(line[-1])
                monkey.truetarget=target
            elif "If false" in line:
                target=int(line[-1])
                monkey.falsetarget=target
                # end of current monkey , save and create a new one
                monkeys.append(monkey)
                monkey=Monkey()


def do_round(monkeys: list[Monkey], number: int):
    #print("Doing round: ",number)
    for monkey in monkeys:
        #print("   Monkey: ",monkey.number)
        for item in monkey.items[:]: # need to operate over copy or remove would fail
            # monkey inspects the item and does operation
            # worry level to be divided by three and rounded down to the nearest integer
            monkey.items.remove(item)
            monkey.inspections+=1
            newitem=monkey.operation(item)//3
            # monkey does test and throws item
            if (newitem%monkey.test == 0):
                target=monkey.truetarget
            else:
                target=monkey.falsetarget
            #print(f"  Throwing {newitem} to {target}")
            monkeys[target].add_item(newitem)


def get_monkey_business(monkeys: list[Monkey]) -> int:
    businesslist=[]
    for monkey in monkeys:
        print(monkey)
        businesslist.append(monkey.inspections)
    businesslist.sort(reverse=True)
    return businesslist[0] * businesslist [1]




monkeys: list[Monkey] = []
readfile()

for i in range(0,NUMROUNDS):
    do_round(monkeys,i)
business=get_monkey_business(monkeys)
print("Monkey business: ", business)


