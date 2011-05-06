#!/usr/bin/env python3
# Project Euler problem 32

from math import sqrt, ceil
from mergesort import mergeSort

def getDivisors(n):
    s = 0
    i = 1
    divisors = []
    limit = ceil(sqrt(n))
    while i <= limit:
        if n % i == 0:
            if (int(n/i)) not in divisors:
                divisors.append(i)
        i += 1
    return divisors

total = 0
n = 1
while n < 10000:
    divisors = getDivisors(n)
    for divisor in divisors:
        digits = [int(d) for d in (str(divisor) + str(int(n/divisor)) + str(n))]
        digits = mergeSort(digits)
        if digits == list(range(1, 10)):
            print(n)
            total += n
            break
    
    n += 1

print(total)

