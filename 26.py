#!/usr/bin/env python3
# Project Euler problem 26

from math import sqrt, ceil

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 3
    limit = ceil(sqrt(n))
    while i <= limit:
        if n % i == 0: return False
        i += 2
    return True

n = 997
while n > 0:
    if isPrime(n):
        c = 1
        while (pow(10, c) - 1) % n != 0:
            c += 1
        if (n - c) == 1: break
    n -= 2

print(n)

