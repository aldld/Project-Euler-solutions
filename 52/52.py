#!/usr/bin/env python3
# Project Euler problem 52

from mergesort import mergeSort

n = 2
while True:
    print(n)
    isSolution = True

    digits = mergeSort([int(d) for d in str(n)])
    for factor in range(1, 7):
        test = mergeSort([int(d) for d in str(n*factor)])
        if digits != test: isSolution = False

    if isSolution:
        print(n)
        break

    n += 1

