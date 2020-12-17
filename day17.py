#!/usr/bin/env python

from collections import defaultdict

one = [-1, 0, 1]

def surrounding(n):
    if n == 0:
        yield tuple()
    else:
        for entry in surrounding(n-1):
            yield (-1,) + entry
            yield (0,) + entry
            yield (1,) + entry

def solve(data, dims):
    around = [coord for coord in surrounding(dims) if any(coord)]
    lines = data.splitlines()
    start = {
        (x, y) + (0,) * (dims-2) for y in range(len(lines)) for x in range(len(lines[0]))
        if lines[y][x] == '#'
    }

    for _ in range(6):
        next = set()
        surround = defaultdict(int)
        for coord in start:
            for dcoord in around:
                ncoord = tuple(i+di for i, di in zip(coord, dcoord))
                surround[ncoord] += 1
        for coord, count in surround.items():
            if coord in start and 2 <= count <= 3:
                next.add(coord)
            elif coord not in start and count == 3:
                next.add(coord)
        start = next

    return len(start)

def part1(data):
    return solve(data, 3)

def part2(data):
    return solve(data, 4)

if __name__ == '__main__':
    data = open('input17.txt').read()
    print(part1(data))
    print(part2(data))
