#!/usr/bin/env python3
# Project Euler problem 56

maximum = 0

for a in range(100):
    for b in range(100):
        digitalSum = sum([int(i) for i in str(a**b)])
        if digitalSum > maximum:
            maximum = digitalSum

print(maximum)

