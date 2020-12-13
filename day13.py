#!/usr/bin/env python

from itertools import count
import math
import re

def part1(data):
    10 % 7 == 3
    14 % 7 == 0

    target, *buses = list(map(int, re.findall(r'\d+', data)))
    nearest = min((math.ceil(target/bus)*bus, bus) for bus in buses)
    return (nearest[0] - target) * nearest[1]

import typing

class Eq(typing.NamedTuple):
    # Linear equation: ax + b
    a: int
    b: int

    def count(self):
        # b, b + a, b + 2a, b + 3a, ...
        return count(-self.b, self.a)

    def simplify(self):
        return Eq(self.a, self.b % self.a)

    def __repr__(self):
        return f'(x + {self.b}) % {self.a}'

class LinearEqs(list):
    def solve(self):
        # Iterate through largest sequence, filtering by the others
        largest, *rest = sorted(self, reverse=True)

        # fast case
        if len(self) == 2:
            eq = rest[0]
            remain = eq.a - eq.b
            for t in largest.count():
                if t % eq.a == remain:
                    return t

        # slow case
        for t in largest.count():
            if all((t + eq.b) % eq.a == 0 for eq in rest):
                return t

    def merge(self):
        # Modular arithmetic
        # (t + x) mod n == 0
        # (t + y + m*i) mod m == 0
        # if x == y + m*i:
        # => (t + y) mod m * n == 0
        result = LinearEqs()
        
        stack = sorted(self, key=lambda eq: eq.b)
        while stack:
            # Get next largest (x + b) component
            top = stack.pop()
            newa = top.a

            # Find any others that can be combined
            for i in reversed(range(len(stack))):
                # If eq (x + b) term is congruent to top (x + b) term, merge it in
                eq = stack[i]
                if (top.b - eq.b) % eq.a == 0:
                    newa *= eq.a
                    stack.pop(i)

            result.append(Eq(newa, top.b))
        return result

def part2(data):
    eqs = LinearEqs(
        Eq(int(bus), i).simplify()
        for i, bus in enumerate(data.splitlines()[-1].split(','))
        if bus != 'x'
    )
    eqs = eqs.merge()
    return eqs.solve()

if __name__ == '__main__':
    data = open('input13.txt').read()
    print(part1(data))
    print(part2(data))
