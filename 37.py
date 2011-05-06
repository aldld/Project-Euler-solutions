#!/usr/bin/env python3
# Project Euler problem 37

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

total = 0
numTruncPrimes = 0
i = 23
while numTruncPrimes < 11:
    if isPrime(i):
        skip = False
        string = str(i)
        digit = 0
        while digit < len(string):
            digit += 1

        if not skip:
            # Left to right
            ltr = str(i)
            while len(ltr) > 0:
                if not isPrime(int(ltr)): break

                l = list(ltr)
                del l[0]
                ltr = ''.join(l)

            rtl = str(i)
            while len(rtl) > 0:
                if not isPrime(int(rtl)): break

                l = list(rtl)
                del l[-1]
                rtl= ''.join(l)

            if (len(rtl) == 0) and (len(ltr) == 0):
                total += i
                numTruncPrimes += 1

    i += 2

print(total)

