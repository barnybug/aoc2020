#!/usr/bin/env python

import numpy as np

def trees(lines, stride):
    ys = np.arange(lines.shape[0])
    xs = (ys * stride) % lines.shape[1]
    return sum(lines[ys,xs])

def parse(data):
    return np.array([list(line) for line in data.split()]) == '#'

def part1(data):
    lines = parse(data)
    return trees(lines, 3)

def part2(data):
    lines = parse(data)
    answers = [
        trees(lines, 1),
        trees(lines, 3),
        trees(lines, 5),
        trees(lines, 7),
        trees(lines[::2], 1),
    ]
    return np.prod(answers)

if __name__ == '__main__':
    data = open('input03.txt').read()
    print(part1(data))
    print(part2(data))
