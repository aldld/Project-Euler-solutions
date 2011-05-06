#!/usr/bin/env python
# Project Euler problem 13

# Load the file into a list
numbers = []
for number in open('numbers.txt', 'r'):
    numbers.append(int(number))

print str(sum(numbers))[0:10]

