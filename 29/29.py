#!/usr/bin/env python3
# Project Euler problem 29

from mergesort import mergeSort

terms = []

for a in range(2, 101):
    for b in range(2, 101):
        terms.append(a**b)

terms = mergeSort(terms)
i = 0
while i < len(terms)-1:
    while terms[i] == terms[i+1]:
        del terms[i+1]
    i += 1

print(len(terms))

