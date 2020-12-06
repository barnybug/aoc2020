#!/usr/bin/env python

def part1(data):
    return sum(
        len(set(group) - {'\n'})
        for group in data.split('\n\n')
    )

def part2(data):
    return sum(
        len(set.intersection(*map(set, group.splitlines())))
        for group in data.split('\n\n')
    )

if __name__ == '__main__':
    data = open('input06.txt').read()
    print(part1(data))
    print(part2(data))
