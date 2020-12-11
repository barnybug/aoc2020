#!/usr/bin/env python

import numpy as np
from scipy.signal import convolve2d

conv = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

def part1(data):
    grid = np.array([list(line) for line in data.splitlines()], dtype='U1')
    mask = (grid == 'L')
    seated = np.zeros(grid.shape, '?')
    while True:
        occupied = convolve2d(seated, conv, mode='same')
        now = (~seated & (occupied == 0) & mask) | (seated & (occupied < 4))
        if np.array_equal(seated, now):
            break
        seated = now
    return seated.sum()

deltas = [
    (x, y)
    for x in (-1, 0, 1) 
    for y in (-1, 0, 1) 
    if x != 0 or y != 0
]

def part2(data):
    grid = np.array([list(line) for line in data.splitlines()], dtype='U1')
    space = (grid == '.')
    mask = (grid == 'L')
    seated = np.zeros(grid.shape, '?')
    while True:
        changed = False
        now = np.copy(seated)
        for x in range(grid.shape[1]):
            for y in range(grid.shape[0]):
                if space[y, x]:
                    continue
                s = seated[y, x]

                surrounding = 0
                for delta in deltas:
                    for i in range(1, 99):
                        at = (y + delta[1] * i, x + delta[0] * i)
                        if at[0] < 0 or at[0] >= grid.shape[0]:
                            break
                        if at[1] < 0 or at[1] >= grid.shape[1]:
                            break
                        if seated[at]:
                            surrounding += 1
                            break
                        if mask[at]:
                            break

                    # bail early
                    if not s and surrounding > 0:
                        break
                    elif s and surrounding >= 5:
                        break
                
                if not s and surrounding == 0:
                    changed = True
                    now[y, x] = True
                elif s and surrounding >= 5:
                    changed = True
                    now[y, x] = False
                # else no change

        if not changed:
            break
        seated = now

    return seated.sum()

if __name__ == '__main__':
    data = open('input11.txt').read()
    print(part1(data))
    print(part2(data))
