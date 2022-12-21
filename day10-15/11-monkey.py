#!/usr/bin/python3

from dataclasses import dataclass
from collections.abc import Callable
from math import lcm


Operation = Callable[[int], int]

@dataclass
class Monkey:
    items: 'list[int]'
    operation: str
    test: str
    truetarget: int
    falsetarget: int
    inspections: int

    def __init__(self):
        self.items=[]
        self.test=""
        self.truetarget=-1
        self.falsetarget=-1
        self.inspections=0

    def add_item(self, item: int):
        self.items.append(item)

    def add_operation(self, opstring: str):
        self.operation=lambda old: eval(opstring.split("=")[-1])


def readfile(filename: str)  -> 'list[Monkey]':
    monkeys: list[Monkey] = []
    monkey=Monkey()
    with open(filename) as inputfile:
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
                _,value=line.split("divisible by ")
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
    return monkeys


def do_round(monkeys: 'list[Monkey]', divisor: int, mod_lcm: int):
    for monkey in monkeys:
        for item in monkey.items[:]: # need to operate over copy or remove would fail
            # monkey inspects the item and does operation
            monkey.items.remove(item)
            monkey.inspections+=1
            if (divisor):  # worry level to be divided by three and rounded down to the nearest integer
                newitem=monkey.operation(item)//divisor
            else: # "need another way to keep worry level managable"
                newitem=monkey.operation(item)%mod_lcm 
            # monkey does test and throws item
            if (newitem%monkey.test == 0):
                target=monkey.truetarget
            else:
                target=monkey.falsetarget
            #print(f"  Throwing {newitem} to {target}")
            monkeys[target].add_item(newitem)


def get_monkey_business(monkeys: 'list[Monkey]') -> int:
    businesslist=[monkey.inspections for monkey in monkeys]
    businesslist.sort(reverse=True)
    return businesslist[0] * businesslist [1]

    

def do_part(rounds, divisor, filename):
    monkeys=readfile(filename)
    mod_lcm=lcm(*[monkey.test for monkey in monkeys])
    #print("LCM: ", mod_lcm)
    for i in range(0,rounds):
        do_round(monkeys, divisor, mod_lcm)
    business=get_monkey_business(monkeys)
    print("Monkey business: ", business)

do_part(rounds=20, divisor=3, filename="11-input.txt")
do_part(rounds=10000, divisor=None, filename="11-input.txt")
