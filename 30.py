#!/usr/bin/env python3
# Project Euler problem 30

total = 0
i = 2
while i < 354294:
    fifthPowerSum = 0
    for digit in str(i):
        fifthPowerSum += int(digit)**5

    if fifthPowerSum == i:
        total += i

    i += 1

print(total)

