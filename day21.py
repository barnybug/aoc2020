#!/usr/bin/env python

from itertools import permutations
import re

def parse_line(line):
    line = re.sub(r'\W+', ' ', line).strip()
    words = line.split()
    contains = words.index('contains')
    return set(words[:contains]), set(words[contains+1:])

def parse(data):
    rules = [parse_line(line) for line in data.splitlines()]
    ingredients = set.union(*[ings for ings, _ in rules])
    allergens = sorted(set.union(*[alls for _, alls in rules]))
    return rules, ingredients, allergens

def inert_ingredients(rules, ingredients, allergens):
    potential_allergens = set()
    for ig in ingredients:
        for al in allergens:
            for igs, als in rules:
                # if the allergen is in one of this rules' ingredients
                if al in als and ig not in igs:
                    break
            else:
                potential_allergens.add(ig)
                break
    return ingredients - potential_allergens

def part1(data):
    rules, ingredients, allergens = parse(data)
    return sum(
        ig in igs
        for igs, _ in rules
        for ig in inert_ingredients(rules, ingredients, allergens)
    )

def part2(data):
    rules, ingredients, allergens = parse(data)
    inert = inert_ingredients(rules, ingredients, allergens)
    # eliminate inert from rules
    for igs, _ in rules:
        [igs.discard(i) for i in inert]
    ingredients -= inert
    assert len(ingredients) == len(allergens)
    # brute force
    for perm in permutations(ingredients):
        ingredient_map = {ig: al for ig, al in zip(perm, allergens)}
        for igs, als in rules:
            calc_als = set(ingredient_map[ig] for ig in igs)
            if not als.issubset(calc_als):
                break
        else:
            return ','.join(perm)
    return None

if __name__ == '__main__':
    data = open('input21.txt').read()
    print(part1(data))
    print(part2(data))
