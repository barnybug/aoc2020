#!/usr/bin/env python

from numba import njit
from numba.typed import List

@njit
def play(cups, times):
    n = max(cups)

    nodes = [0] * (n+1)
    for i in range(n):
        nodes[cups[i]] = cups[(i+1) % n]

    current = cups[0]
    for i in range(times):
        a = nodes[current]
        b = nodes[a]
        c = nodes[b]
        nodes[current] = nodes[c]
        destination = current
        while True:
            destination -= 1
            if destination < 1:
                destination = n
            if destination != a and destination != b and destination != c:
                break
        
        nodes[c] = nodes[destination]
        nodes[destination] = a
        current = nodes[current]
    
    i = 1
    while True:
        i = nodes[i]
        if i == 1:
            break
        yield i

def part1(data):
    cups = List(map(int, data))
    cups = play(cups, 100)
    return ''.join(map(str, cups))

def part2(data):
    cups = List(map(int, data))
    for i in range(9, 1000000):
        cups.append(i+1)
    it = play(cups, 10000000)
    return next(it) * next(it)

if __name__ == '__main__':
    data = '253149867'
    print(part1(data))
    print(part2(data))
