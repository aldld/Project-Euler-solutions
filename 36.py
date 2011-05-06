#!/usr/bin/env python3
# Project Euler problem 36

x = 1
total = 0

while x < 1000000:
    n = x
    binDigits = []
    while int(n) / 2 != 0:
        binDigits.append(int(n) % 2)
        n = int(n) / 2

    if (binDigits == binDigits[::-1]) and (str(x) == str(x)[::-1]):
        #print(x, ''.join([str(i) for i in binDigits[::-1]]))
        total += x

    x += 2

print(total)

