#!/usr/bin/env python

import operator
import parsimonious

grammar1 = parsimonious.Grammar('''
expr = add / term
add = term (op term)+
op = ~" [+*] "
term = nested / number
nested = "(" expr ")"
number = ~"[0-9]+"
''')

class Visitor1(parsimonious.NodeVisitor):
    def visit_number(self, node, children):
        return int(node.text)

    def visit_add(self, node, children):
        a, right = children
        for op, b in right:
            a = op(a, b)
        return a

    def visit_expr(self, node, children):
        return children[0]

    def visit_term(self, node, children):
        if len(children) == 1:
            return children[0]

    def visit_op(self, node, children):
        return operator.add if node.text == ' + ' else operator.mul
    
    def visit_nested(self, node, children):
        return children[1]

    def generic_visit(self, node, children):
        """ The generic visit method. """
        return children

def part1(data: str):
    visitor = Visitor1()
    return sum(
        visitor.visit(grammar1.parse(line))
        for line in data.splitlines()
    )

grammar2 = parsimonious.Grammar('''
expr = mul / term
mul = term " * " expr
term = add / number / nested
add = number_or_nested " + " term
number_or_nested = nested / number
nested = "(" expr ")"
number = ~"[0-9]+"
''')

class Visitor2(parsimonious.NodeVisitor):
    def visit_expr(self, node, children):
        return children[0]

    def visit_mul(self, node, children):
        a, _, b = children
        return a * b

    def visit_term(self, node, children):
        return children[0]

    def visit_add(self, node, children):
        a, _, b = children
        return a + b

    def visit_number_or_nested(self, node, children):
        return children[0]

    def visit_nested(self, node, children):
        return children[1]

    def visit_number(self, node, children):
        return int(node.text)

    def generic_visit(self, node, children):
        """ The generic visit method. """
        return children

def part2(data):
    visitor = Visitor2()
    return sum(
        visitor.visit(grammar2.parse(line))
        for line in data.splitlines()
    )

if __name__ == '__main__':
    data = open('input18.txt').read()
    print(part1(data))
    print(part2(data))
