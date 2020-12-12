#!/usr/bin/env python

from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int = 0
    y: int = 0

    def __add__(self, d):
        return Coordinate(self.x + d.x, self.y + d.y)

    def __mul__(self, n):
        return Coordinate(self.x * n, self.y * n)

    def turn(self, sign):
        return Coordinate(-sign * self.y, sign * self.x)

N = Coordinate(0, -1)
S = Coordinate(0, 1)
E = Coordinate(1, 0)
W = Coordinate(-1, 0)
COMPASS = {'N': N, 'S': S, 'E': E, 'W': W,}

class Ship:
    def __init__(self, d, waypoint=False):
        self.pos = Coordinate()
        self.d = d
        self.waypoint = waypoint

    def turn(self, times, sign):
        for _ in range(times):
            self.d = self.d.turn(sign)

    def forward(self, n):
        self.pos += self.d * n

    def move(self, delta):
        if self.waypoint:
            self.d += delta
        else:
            self.pos += delta

    def instruction(self, line):
        c = line[0]
        n = int(line[1:])
        if c in COMPASS:
            self.move(COMPASS[c] * n)
        elif c in 'LR':
            self.turn(n//90, -1 if c == 'L' else 1)
        elif c == 'F':
            self.forward(n)

    def manhattan(self):
        return abs(self.pos.x) + abs(self.pos.y)

def part1(data):
    ship = Ship(d=E)
    for line in data.splitlines():
        ship.instruction(line)
    return ship.manhattan()

def part2(data):
    ship = Ship(d=E*10 + N, waypoint=True)
    for line in data.splitlines():
        ship.instruction(line)
    return ship.manhattan()

if __name__ == '__main__':
    data = open('input12.txt').read()
    print(part1(data))
    print(part2(data))
