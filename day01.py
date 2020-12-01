#!/usr/bin/env python

from itertools import combinations
from math import prod

def solve(data, n):
    numbers = list(map(int, data))
    for draw in combinations(numbers, n):
        if sum(draw) == 2020:
            return prod(draw)

def part1(data):
    return solve(data, 2)

def part2(data):
    return solve(data, 3)

if __name__ == '__main__':
    print(part1(open('input01.txt')))
    print(part2(open('input01.txt')))
