#!/usr/bin/env python3
# Project Euler problem 97

# Calculate the last ten digits of 2^7830457
i = 1
n = 2
while i <= 7830457:
    print(i, n)
    n = n * 2
    if len(str(n)) > 10:
        n = int(str(n)[-10:])
    i += 1

print(n)

