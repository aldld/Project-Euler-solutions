#!/usr/bin/env python3
# Project Euler problem 21

from math import ceil

def d(n):
    s = 0
    i = 1
    while i <= ceil(n/2):
        if n % i == 0:
            s += i
        i += 1

    return s

s = 0
i = 1
amicables = []
while i < 10000:
    print(i)
    if i not in amicables:
        a = d(i)
        if d(a) == i and i != a:
            s += a + i
            amicables.append(a)
            amicables.append(i)

    i += 1

print(amicables)
print(s)
print(sum(amicables))

