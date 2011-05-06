#!/usr/bin/env python3
# Project Euler problem 14

tested = {} # starting number: length

startNumber = 2
while startNumber < 1000000:
    n = startNumber
    #print(startNumber)
    seqLength = 1
    while n > 1:
        seqLength += 1
        if (n % 2) == 0: n = n / 2
        else: n = 3*n + 1

        try: tested[n]
        except KeyError: continue
        else:
            seqLength += tested[n]
            break

    tested[startNumber] = seqLength
    startNumber += 1

i = 2
g = 2
while i < 1000000:
    if tested[i] > tested[g]: g = i
    i += 1

print(g)

