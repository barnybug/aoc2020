#!/usr/bin/env python

import re

def compile(rules, key):
    rule = rules[key]
    if rule.startswith('"'):
        return rule.strip('"')
    
    rule = re.sub(r'\d+', lambda m: compile(rules, m.group(0)), rule)
    rule = rule.replace(' ', '')
    if '|' in rule:
        rule = '(?:%s)' % rule
    return rule

def parse(data):
    rules, messages = data.split('\n\n')
    rules = dict(
        rule.split(': ')
        for rule in rules.splitlines()
    )
    return rules, messages

def part1(data):
    rules, messages = parse(data)
    regex = compile(rules, '0')
    regex = re.compile(regex)
    return sum(bool(regex.fullmatch(line)) for line in messages.splitlines())

def part2(data):
    rules, messages = parse(data)
    # 8: 42 | 42 8
    rules['8'] = '42+'
    # 11: 42 31 | 42 11 31
    rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31'
    regex = compile(rules, '0')
    regex = re.compile(regex)
    return sum(bool(regex.fullmatch(line)) for line in messages.splitlines())

if __name__ == '__main__':
    data = open('input19.txt').read()
    print(part1(data))
    print(part2(data))
