#!/usr/bin/env python3
# Project Euler problem 22

from mergesort import mergeSort

alphabet = list(map(chr, range(65, 91)))

names = []

f = open('names.txt')
names = f.read().replace('"', '').split(',')
names = mergeSort(names)

total = 0
i = 0
while i < len(names):
    score = 0
    for letter in names[i]:
        j = 0
        while j < len(alphabet):
            if alphabet[j] == letter:
                score += j + 1
            j += 1

    score = score * (i + 1)
    total += score
    i += 1

print(total)

