#!/usr/bin/env python

import re
from collections import defaultdict

def part1(data):
    graph = defaultdict(set)
    for rule in data.splitlines():
        m = re.match(r'(.+?) bags contain (.+)\.', rule)
        left, rights = m.groups()
        for right in re.findall(r'\d+ (.+?) bag', rights):
            graph[right].add(left)

    start = 'shiny gold'
    q = [start]
    visited = set()
    while q:
        current = q.pop(0)
        unvisited = graph[current] - visited
        visited.update(unvisited)
        q.extend(unvisited)

    return len(visited)

def part2(data):
    contains = {}
    for rule in data.splitlines():
        left, rights = rule.split(' bags contain ', 1)
        # no other bags matched nothing
        contains[left] = [
            (int(number), right)
            for number, right in re.findall(r'(\d+) (.+?) bag', rights)
        ]

    resolved = {}
    def resolve(key):
        if key not in resolved:
            resolved[key] = 1 + sum(n * resolve(bag) for n, bag in contains[key])
        return resolved[key]

    return resolve('shiny gold')-1

if __name__ == '__main__':
    data = open('input07.txt').read()
    print(part1(data))
    print(part2(data))
