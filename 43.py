#!/usr/bin/env python3
# Project Euler problem 43

from math import factorial

digits = list(range(10))

total = 0

i = 0
while i < (factorial(9))**2:
    string = ''.join([str(d) for d in digits])
    
    hasProperty = True
    if int(string[1] + string[2] + string[3]) % 2 != 0:
        hasProperty = False
    if int(string[2] + string[3] + string[4]) % 3 != 0:
        hasProperty = False
    if int(string[3] + string[4] + string[5]) % 5 != 0:
        hasProperty = False
    if int(string[4] + string[5] + string[6]) % 7 != 0:
        hasProperty = False
    if int(string[5] + string[6] + string[7]) % 11 != 0:
        hasProperty = False
    if int(string[6] + string[7] + string[8]) % 13 != 0:
        hasProperty = False
    if int(string[7] + string[8] + string[9]) % 17 != 0:
        hasProperty = False

    if hasProperty:
        print(string)
        total += int(string)
    

    # Find the largest index k s.t. digits[k] < digits[k+1]
    j = 0
    k = j
    while j < len(digits) - 1:
        if digits[j] < digits[j+1]:
            k = j
        j += 1

    # Find the largest index l s.t. digits[k] < digits[l]
    j = 0
    l = j
    while j < len(digits):
        if digits[k] < digits[j]:
            l = j
        j += 1

    # Swap digits[k] with digits[l]
    digits[k], digits[l] = digits[l], digits[k]

    # Reverse sequence from digits[k+1] to end
    digits[(k+1):len(digits)] = digits[(k+1):len(digits)][::-1]

    i += 1

print(total)

