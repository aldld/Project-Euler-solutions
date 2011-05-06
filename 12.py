#!/usr/bin/end python
# Project Euler problem 12

triangle = 1
number = 1
while True:
    number += 1
    triangle += number
    numDivisors = 0
    i = 1
    while i < triangle/2:
        if triangle % i == 0: numDivisors += 1
        i += 1

    print triangle, numDivisors

    if numDivisors > 500:
        print triangle
        break

