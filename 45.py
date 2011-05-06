#!/usr/bin/env python3
# Project Euler problem 45

from math import sqrt

n = 144
while True:
    # Generate a hexagonal number
    i = n * (2*n - 1)

    # Check if pentagonal
    pentagonal = False
    t = (sqrt(0.25 + 6*i) + 0.5) / 3
    if (int(t) == t) and (t > 0):
        pentagonal = True
    m = (-1*sqrt(0.25 + 6*i) + 0.5) / 3
    if (int(m) == m) and (m > 0):
        pentagonal = True

    if pentagonal:
        print(i)
        break

    n += 1

