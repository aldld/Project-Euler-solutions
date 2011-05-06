#!/usr/bin/env python3
# Project Euler problem 23

from math import ceil

# Memoize sums of divisors here
precomputedD = {}

def d(n):
    global precomputedD
    if n not in precomputedD:
        s = 0
        i = 1
        while i <= ceil(n/2):
            if n % i == 0:
                s += i
            i += 1

        precomputedD[n] = s
    else:
        s = precomputedD[n]

    return s

total = 0

n = 1
while n < 28123:
    sumOfAbundants = False
    i = 1
    while i <= ceil(n/2):
        if (d(i) > i) and (d(n-i) > (n-i)):
            sumOfAbundants = True
            break
        i += 1

    if not sumOfAbundants:
        print(n)
        total += n
        print('----->', total)

    n += 1

