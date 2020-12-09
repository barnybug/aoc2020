#!/usr/bin/env python

def part1(data, preamble=25):
    numbers = list(map(int, data.splitlines()))
    for i in range(preamble, len(numbers)):
        pairs = (
            numbers[a]+numbers[b]
            for a in range(i-preamble, i-1)
            for b in range(a+1, i)
        )
        if numbers[i] not in pairs:
            return numbers[i]
    return None

def part2(data, preamble=25):
    numbers = list(map(int, data.splitlines()))
    answer = part1(data, preamble)
    for i in range(len(numbers)):
        s = 0
        for j in range(i, len(numbers)):
            s += numbers[j]
            if s == answer:
                return min(numbers[i:j+1]) + max(numbers[i:j+1])
            if s > answer:
                break # bailout early
    return None

if __name__ == '__main__':
    data = open('input09.txt').read()
    print(part1(data))
    print(part2(data))
