#!/usr/bin/env python

from numba import njit
from numba.typed import List

def solve(data, nth):
    return jit_solve(List(data), nth)

@njit
def jit_solve(data, nth):
    seen = {}
    for i, n in enumerate(data):
        seen[n] = i
    last = 0
    for i in range(len(data), nth-1):
        try:
            seen[last], last = i, i - seen[last]
        except:
            seen[last], last = i, 0
    return last
    
def part1(data):
    return solve(data, 2020)

def part2(data):
    return solve(data, 30000000)

if __name__ == '__main__':
    data = open('input15.txt').read()
    input = [0,5,4,1,10,14,7]
    print(part1(input))
    print(part2(input))
