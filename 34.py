#!/usr/bin/env python3
# Project Euler problem 34

from math import factorial

total = 0
i = 3
while i < 2540160:
    factorialSum = 0
    for digit in str(i):
        factorialSum += factorial(int(digit))

    if factorialSum == i:
        total += i
        print(i)

    i += 1

print(total)

