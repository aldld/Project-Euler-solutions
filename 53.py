#!/usr/bin/env python3
# Project Euler problem 53

from math import factorial

count = 0
n = 0
while n <= 100:
    r = 0
    while r <= n:
        if factorial(n)/(factorial(r)*factorial(n-r)) > 1000000:
            count += 1
        r += 1
    n += 1

print(count)

