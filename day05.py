#!/usr/bin/env python

def seat_id(line):
    binary = ['1' if c in ('B', 'R') else '0' for c in line]
    return int(''.join(binary), 2)

def part1(data):
    return max(seat_id(line) for line in data.splitlines())

def part2(data):
    seat_ids = sorted(seat_id(line) for line in data.splitlines())
    for a, b in zip(seat_ids, seat_ids[1:]):
        if a+2 == b:
            return a+1

if __name__ == '__main__':
    data = open('input05.txt').read()
    print(part1(data))
    print(part2(data))
