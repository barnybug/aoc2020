#!/usr/bin/env python

import re

def parse(line):
    a, b, letter, pw = re.split(r'\W+', line.strip())
    a, b = int(a), int(b)
    return a, b, letter, pw

def valid1(line):
    a, b, letter, pw = parse(line)
    return a <= pw.count(letter) <= b

def part1(data):
    return sum(valid1(line) for line in data)

def valid2(line):
    a, b, letter, pw = parse(line)
    return (pw[a-1]+pw[b-1]).count(letter) == 1

def part2(data):
    return sum(valid2(line) for line in data)

if __name__ == '__main__':
    data = list(open('input02.txt'))
    print(part1(data))
    print(part2(data))
