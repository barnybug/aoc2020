#!/usr/bin/env python

import math

def modlog(g, h, p):
    # Baby-step, giant-step algorithm for solving discrete modular logarithms
    # g^k = h mod p
    N = int(math.ceil(math.sqrt(p-1)))
    t = {}
    for i in range(N):
        t[pow(g, i, p)]=i

    c = pow(g, -N, p)
    
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in t: 
            return j * N + t[y]
    return None    

MOD = 20201227

def part1(a, b):
    k = modlog(7, a, MOD)
    return pow(b, k, MOD)

if __name__ == '__main__':
    print(part1(11239946, 10464955))
