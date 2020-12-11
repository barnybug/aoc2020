#!/usr/bin/env python

import pdb
from grid import Grid

def part1(data):
    grid = Grid.parse(data.splitlines())
    while True:
        changed = False
        step = Grid()
        for xy in grid.range():
            c = grid[xy]
            if c == '.':
                continue
            surrounding = sum(c == '#' for c in grid.adjacent(xy))
            if c == 'L' and surrounding == 0:
                changed = True
                step[xy] = '#'
            elif c == '#' and surrounding >= 4:
                changed = True
                step[xy] = 'L'
            else:
                step[xy] = c

        if not changed:
            break
        grid = step

    return grid.count()['#']

deltas = [
    (x, y)
    for x in (-1, 0, 1) 
    for y in (-1, 0, 1) 
    if x != 0 or y != 0
]

def part2(data):
    grid = Grid.parse(data.splitlines())
    while True:
        changed = False
        step = Grid()
        for xy in grid.range():
            c = grid[xy]
            if c == '.':
                continue

            surrounding = 0
            for delta in deltas:
                for i in range(1, 99):
                    at = (xy[0] + delta[0] * i, xy[1] + delta[1] * i)
                    if at[0] not in grid.xrange() or at[1] not in grid.yrange():
                        break
                    atc = grid[at]
                    if atc == '.':
                        continue
                    if atc == '#':
                        surrounding += 1
                    break
            
            if c == 'L' and surrounding == 0:
                changed = True
                step[xy] = '#'
            elif c == '#' and surrounding >= 5:
                changed = True
                step[xy] = 'L'
            else:
                step[xy] = c

        if not changed:
            break
        grid = step

    return grid.count()['#']

if __name__ == '__main__':
    data = open('input11.txt').read()
    # print(part1(data))
    print(part2(data))
