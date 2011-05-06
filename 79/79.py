#!/usr/bin/env python3
# Project Euler problem 79

from math import factorial
from mergesort import mergeSort

charsUsed = ''
randChars = []
passcode = []

f = open('keylog.txt')
line = f.readline()
while line != '':
    charsUsed += line[0] + line[1] + line[2]
    randChars.append(line)
    line = f.readline()
charsUsed = list(charsUsed)

# Generate an array of all digits used in the passcode
charsUsed = mergeSort(charsUsed)
i = 0
length = len(charsUsed)
while i < length - 1:
    try:
        while charsUsed[i] == charsUsed[i+1]:
            del charsUsed[i+1]
            length -= 1
    except IndexError:
        pass
    i += 1

i = 0
s = []
while i < factorial(len(charsUsed)):
    # Find the largest index k s.t. charsUsed[k] < charsUsed[k+1]
    j = 0
    k = j
    while j < len(charsUsed) - 1:
        if charsUsed[j] < charsUsed[j + 1]:
            k = j
        j += 1

    # Find the largest index l s.t. charsUsed[k] < charsUsed[l]
    j = 0
    l = 0
    while j < len(charsUsed):
        if charsUsed[k] < charsUsed[j]:
            l = j
        j += 1

    # Swap charsUsed[k] with charsUsed[l]
    charsUsed[k], charsUsed[l] = charsUsed[l], charsUsed[k]

    # Reverse sequence from charsUsed[k+1] to end
    charsUsed[(k+1):len(charsUsed)] = charsUsed[(k+1):len(charsUsed)][::-1]

    satisfiedConditions = 0
    for chars in randChars:
        firstPos = 0
        secondPos = 0
        thirdPos = 0

        j = 0
        while j < len(charsUsed):
            if int(charsUsed[j]) == int(chars[0]):
                firstPos = j
            if int(charsUsed[j]) == int(chars[1]):
                secondPos = j
            if int(charsUsed[j]) == int(chars[2]):
                thirdPos = j
            j += 1

        if (firstPos < secondPos) and (secondPos < thirdPos):
            satisfiedConditions += 1
        else: break

    s.append(satisfiedConditions)

    if satisfiedConditions >= len(randChars):
        print(''.join([str(c) for c in charsUsed]))
    i += 1

print(max(s))

