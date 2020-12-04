#!/usr/bin/env python

import re

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def between(a, b, suffix=''):
    return {str(i)+suffix for i in range(a, b+1)}

validation = {
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    'byr': between(1920, 2002),
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    'iyr': between(2010, 2020),
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    'eyr': between(2020, 2030),
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    'hgt': between(150, 193, 'cm') | between(59, 76, 'in'),
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    'hcl': re.compile(r'#[0-9a-f]{6}$'),
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    'ecl': {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    'pid': re.compile(r'\d{9}$'),
    # cid (Country ID) - ignored, missing or not.
    'cid': True,
}

def validate_field(field, value):
    rule = validation[field]
    if isinstance(rule, set):
        return value in rule
    elif isinstance(rule, re.Pattern):
        return rule.match(value)
    else:
        return rule

class Passport:
    def __init__(self, data):
        parts = [pair.split(':') for pair in data.split()]
        self.fields = {a: b for a, b in parts}

    def fields_present(self):
        return set(self.fields).issuperset(required)

    def fields_valid(self):
        return all(validate_field(field, value) for field, value in self.fields.items())

def part1(data):
    passports = map(Passport, data.split('\n\n'))
    return sum(
        passport.fields_present()
        for passport in passports
    )

def part2(data):
    passports = map(Passport, data.split('\n\n'))
    return sum(
        passport.fields_present() and passport.fields_valid()
        for passport in passports
    )

if __name__ == '__main__':
    data = open('input04.txt').read()
    print(part1(data))
    print(part2(data))
