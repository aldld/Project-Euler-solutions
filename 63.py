#!/usr/bin/env python3
# Project Euler problem 63

number = 0
i = 0
while i < 1000000000:
    print(i)
    n = len(str(i))
    base = i**(1/n)
    if int(base) == base:
        print(i)
        number += 1

    i += 1

print(number)

