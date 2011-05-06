#!/usr/bin/env python3
# Project Euler problem 41

from math import sqrt, ceil, factorial

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

numDigits = 4
maxPrime = 2143
while numDigits < 10:
    digits = list(range(1, numDigits + 1))
    
    i = 0
    while i < factorial(len(digits)):
        # Find the largest index k s.t. digits[k] < digits[k + 1]
        j = 0
        k = j
        while j < len(digits) - 1:
            if digits[j] < digits[j+1]:
                k = j
            j += 1

        # Find the largest index l s.t. digits[k] < digits[l]
        j = 0
        l = 0
        while j < len(digits):
            if digits[k] < digits[j]:
                l = j
            j += 1

        # Swap digits[k] with digits[l]
        digits[k], digits[l] = digits[l], digits[k]

        # Reverse sequence from digits[k+1] to end
        digits[(k+1):len(digits)] = digits[(k+1):len(digits)][::-1]

        #print(''.join([str(d) for d in digits]))

        n = int(''.join([str(d) for d in digits]))
        if isPrime(n) and (n > maxPrime):
            maxPrime = n

        i += 1
    #input()
    
    numDigits += 1

print(maxPrime)
