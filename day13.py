#!/usr/bin/env python

from itertools import count
import math
import re

def part1(data):
    target, *buses = list(map(int, re.findall(r'\d+', data)))
    nearest = min((math.ceil(target/bus)*bus, bus) for bus in buses)
    return (nearest[0] - target) * nearest[1]

def chinese_remainder_theorem(eqs):
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = int(math.prod(n for _, n in eqs))
    x = sum(a * N//n * pow(N//n, -1, n) for a, n in eqs)
    return x % N

def part2(data):
    # Buses timings are a series of constraints:
    # t + 0 = 0 mod b1, t + 1 = 0 mod b2, ...
    # So solve for (Chinese Remainder Theorem):
    # t = 0 mod b1, t = 1 mod b2, etc.
    # b1, b2 should be co-prime (which fortunately they are)
    eqs = [(-i, int(b)) for i, b in enumerate(data.splitlines()[-1].split(',')) if b != 'x']
    return chinese_remainder_theorem(eqs)

if __name__ == '__main__':
    data = open('input13.txt').read()
    print(part1(data))
    print(part2(data))
