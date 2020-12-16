#!/usr/bin/env python

import math
import re
from typing import NamedTuple

def numbers(line):
    return [int(n) for n in re.findall(r'\d+', line)]

class Rule(NamedTuple):
    name: str
    a: int
    b: int
    c: int
    d: int

    def valid_set(self):
        return set(range(self.a, self.b+1)) | set(range(self.c, self.d+1))

def parse_rules(data):
    rules = data.split('\n\n')[0]
    return [
        Rule(name, int(a), int(b), int(c), int(d))
        for name, a, b, c, d in re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rules)
    ]

def part1(data):
    rules = parse_rules(data)
    valid = set()
    for rule in rules:
        valid.update(rule.valid_set())
    _, _, nearby_tickets = data.split('\n\n')
    return sum(n for n in numbers(nearby_tickets) if n not in valid)

def parse_tickets(data):
    _, _, nearby_tickets = data.split('\n\n')
    return [numbers(line) for line in nearby_tickets.splitlines()[1:]]

def field_order(data):
    _, _, nearby_tickets = data.split('\n\n')
    rules = parse_rules(data)

    nearby_tickets = [numbers(line) for line in nearby_tickets.splitlines()[1:]]
    # discard invalid tickets
    all_numbers = set.union(*(rule.valid_set() for rule in rules))
    nearby_tickets = [ticket for ticket in nearby_tickets if all_numbers.issuperset(ticket)]

    field_names = {i: rule.name for i, rule in enumerate(rules)}
    fields = range(len(rules))
    columns = range(len(rules))
    column_to_field = [None] * len(rules)
    column_values = [[ticket[column] for ticket in nearby_tickets] for column in columns]
    potential_fields = [
        (col, {field for field, rule in enumerate(rules) if rule.valid_set().issuperset(column_values[col])})
        for col in columns
    ]
    while potential_fields:
        potential_fields.sort(key=lambda i: len(i[1]))
        column, fields = potential_fields.pop(0)
        assert len(fields) == 1 # assume it's easy to solve!
        
        field = list(fields)[0]
        column_to_field[column] = field_names[field]
        # eliminate from others
        potential_fields = [
            (c, f - {field})
            for c, f in potential_fields
            if c != column
        ]

    return column_to_field

def part2(data):
    your_ticket = numbers(data.split('\n\n')[1].splitlines()[1])
    column_to_field = field_order(data)
    departure_values = [
        your_ticket[i]
        for i, field in enumerate(column_to_field)
        if field.startswith('departure ')
    ]
    return math.prod(departure_values)

if __name__ == '__main__':
    data = open('input16.txt').read()
    print(part1(data))
    print(part2(data))
