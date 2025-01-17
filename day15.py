#!/usr/bin/env python

import numpy as np
from numba import njit, uint32
from numba.typed import List

def solve(data, nth):
    return jit_solve(List(data), nth)

@njit
def jit_solve(data, nth):
    seen = np.zeros(nth, uint32)
    for i, n in enumerate(data):
        seen[n] = i+1
    last = 0
    for i in range(len(data)+1, nth):
        seen[last], last = i, (i - seen[last] if seen[last] else 0)
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
