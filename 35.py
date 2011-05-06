#!/usr/bin/env python3
# Project Euler problem 35

from math import sqrt, ceil

def isPrime(x):
    if (x == 0) or (x == 1): return False
    if (x == 2) or (x == 3): return True
    if x % 2 == 0: return False

    limit = ceil(sqrt(x))
    i = 3
    while i <= limit:
        if x % i == 0: return False
        i += 2

    return True

count = 0
i = 1
while i < 1000000:
    skip = False
    for digit in str(i):
        digit = int(digit)
        if ((digit % 2 == 0) or (digit == 5)) and len(str(i)) != 1:
            skip = True
            break
    if not isPrime(i): skip = True
    if skip:
        i += 1
        continue

    circular = True

    string = str(i)
    origString = string
    for j in range(len(str(i)) + 1):
        string = origString[j:] + origString[0:j]
        if not isPrime(int(string)):
            circular = False
            break

    if circular:
        print(i)
        count += 1

    i += 1

print(count)

