#!/usr/bin/env python

def run(code):
    acc = 0
    pc = 0
    pcs = set()
    while pc < len(code):
        if pc in pcs:
            return acc, True
        pcs.add(pc)
        op, num = code[pc]
        if op == 'acc':
            acc += int(num)
        pc += int(num) if op == 'jmp' else 1
    return acc, False

def part1(data):
    code = [line.split() for line in data.splitlines()]
    acc, _ = run(code)
    return acc

def part2(data):
    code = [line.split() for line in data.splitlines()]
    for i, ins in enumerate(code):
        if ins[0] == 'acc':
            continue
        code[i] = ('jmp' if ins[0] == 'nop' else 'nop', ins[1])
        acc, loop = run(code)
        if not loop:
            return acc
        code[i] = ins

if __name__ == '__main__':
    data = open('input08.txt').read()
    print(part1(data))
    print(part2(data))
