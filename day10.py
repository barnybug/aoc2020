#!/usr/bin/env python

from itertools import groupby
from math import prod

def diff(data):
    numbers = [0] + list(map(int, data.split()))
    numbers.sort()
    numbers.append(numbers[-1]+3) # end
    return [(b-a) for a, b in zip(numbers, numbers[1:])]

def part1(data):
    diffs = diff(data)
    return diffs.count(1) * diffs.count(3)

def count_one_groups(diffs):
    for i, group in groupby(diffs):
        if i == 1:
            yield len(list(group))

def part2(data):
    diffs = diff(data)
    assert 2 not in diffs # The differences are only 1 or 3.
    # A 3-differences pin both in the pair as required, so problem breaks down into combinations of the isolated 1 groups.
    ones = list(count_one_groups(diffs))
    # Size of the 1-group determines how many combinations this individual group contributes.
    # 1x1: 1 (0 1)
    # 2x1: 2 (0 1 2 or 0 2)
    # 3x1: 4 (0 1 2 3, 0 1 3, 0 2 3, 0 3)
    # 4x1: 7 (0 1 2 3 4, 0 1 2 4, 0 1 3 4, 0 2 3 4, 0 1 4, 0 2 4, 0 3 4)
    # (nothing larger encountered)
    combs = [0, 1, 2, 4, 7]
    # Finally, multiply up the separate combinations.
    return prod(combs[i] for i in ones)

if __name__ == '__main__':
    data = open('input10.txt').read()
    print(part1(data))
    print(part2(data))
