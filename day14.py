#!/usr/bin/env python

from functools import reduce
from operator import or_
import re

def part1(data):
    memory = {}
    maskmask = 0
    maskval = 0
    for line in data.splitlines():
        if m := re.match(r'mask = (.+)', line):
            bitmask = m.group(1)
            maskmask = int(bitmask.replace('1', '0').replace('X', '1'), 2)
            maskval = int(bitmask.replace('X', '0'), 2)
        elif m := re.match(r'mem\[(\d+)\] = (.+)', line):
            addr, value = map(int, m.groups())
            memory[addr] = (value & maskmask) | maskval

    return sum(memory.values())

def part2(data):
    memory = {}
    ones = 0
    mask = 0
    floating = []
    for line in data.splitlines():
        if m := re.match(r'mask = (.+)', line):
            bitmask = m.group(1)
            ixs = [len(bitmask)-1 - m.start() for m in re.finditer('X', bitmask)]
            ixs.reverse()
            floatlen = len(ixs)
            mask = int(''.join('1' if b == '0' else '0' for b in bitmask), 2)
            ones = int(''.join('1' if b == '1' else '0' for b in bitmask), 2)
            floating = [
                reduce(or_, ((fuzz & (1<<i)) << (ixs[i]-i) for i in range(floatlen)))
                for fuzz in range(1<<floatlen)
            ]

        elif m := re.match(r'mem\[(\d+)\] = (.+)', line):
            addr, value = map(int, m.groups())
            for float in floating:
                faddr = (addr & mask) | ones | float
                memory[faddr] = value

    return sum(memory.values())

if __name__ == '__main__':
    data = open('input14.txt').read()
    print(part1(data))
    print(part2(data))
