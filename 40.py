#!/usr/bin/env python3
# Project Euler problem 40

total = 1
digits = ''.join([str(n) for n in range(1, 1000001)])

for i in range(1, 7):
    total *= int(digits[10**i - 1])

print(total)

