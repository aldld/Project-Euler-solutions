#!/usr/bin/env python3
# Project Euler problem 27

from math import sqrt, ceil

def isPrime(n):
    if (n == 0) or (n == 1): return False
    if (n == 2): return True
    if n % 2 == 0: return False

    limit = ceil(sqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0: return False
        i += 2
    return True

coefsPrimes = [] # Format [a, b, numPrimes]
b = 3
while b < 1000:
    if isPrime(b):
        a = -999
        while a < 1000:
            primesGenerated = 0
            n = 0
            while n*n + a*n + b > 0:
                if isPrime(n*n + a*n + b):
                    primesGenerated += 1
                    n += 1
                else: break
            coefsPrimes.append([a, b, primesGenerated])
            a += 1

    b += 2

maxNumPrimes = 0
maxA = 0
maxB = 0
for coefs in coefsPrimes:
    if coefs[2] > maxNumPrimes:
        maxA = coefs[0]
        maxB = coefs[1]
        maxNumPrimes = coefs[2]

print(maxA*maxB)

