#!/usr/bin/env python3
# Project Euler problem 39

from math import sqrt

maxSolnP = 1
maxSolns = 0

for p in range(1, 1001):
    print(p)
    numSolutions = 0
    for a in range(1, p):
        for b in range(1, p-a):
            c = sqrt(a*a + b*b)
            if a + b + c == p:
                numSolutions += 1

    if numSolutions > maxSolns:
        maxSolnP = p
        maxSolns = numSolutions

print(maxSolnP)

