#!/usr/bin/env python3
# Project Euler problem 42

from math import sqrt

alphabet = list(map(chr, range(65, 91)))

f = open('words.txt')
words = f.read().replace('"', '').split(',')

count = 0
index = 0
while index < len(words):
    word = words[index]
    value = 0
    for letter in word:
        j = 0
        while j < len(alphabet):
            if alphabet[j] == letter:
                value += j + 1
                break
            j += 1

    term = sqrt(0.25 + 2*value) + 0.5
    if int(term) == term:
        count += 1

    index += 1

print(count)

