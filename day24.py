#!/usr/bin/env python

import re
from collections import Counter

STEPS = {
    'e': (2, 0),
    'se': (1, 1),
    'sw': (-1, 1),
    'w': (-2, 0),
    'nw': (-1, -1),
    'ne': (1, -1),
}
def run_steps(data):
    grid = set()
    for line in data.splitlines():
        x, y = 0, 0
        for m in re.finditer(r'e|se|sw|w|nw|ne', line):
            step = STEPS[m.group(0)]
            x += step[0]
            y += step[1]

        if (x,y) in grid:
            grid.remove((x,y))
        else:
            grid.add((x,y))
    return grid

def part1(data):
    grid = run_steps(data)
    return len(grid)

def part2(data):
    grid = run_steps(data)
    for _ in range(100):
        adjacent = Counter(
            (x + step[0], y + step[1])
            for x, y in grid
            for step in STEPS.values()
        )
        newgrid = {
            c
            for c, count in adjacent.items()
            if count == 2 or (c in grid and count == 1)
        }
        grid = newgrid
    return len(grid)

if __name__ == '__main__':
    data = open('input24.txt').read()
    print(part1(data))
    print(part2(data))
