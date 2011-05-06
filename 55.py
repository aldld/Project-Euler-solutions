#!/usr/bin/env python3
# Project Euler problem 55

count = 0
i = 1
while i < 10000:
    j = 0
    test = int(str(i)[::-1]) + i
    while (str(test) != str(test)[::-1]) and (j < 50):
        test = int(str(test)[::-1]) + test
        j += 1

    if j >= 50:
        count += 1
    else:
        print(test)

    i += 1

print(count)

