#!/usr/bin/env python3
# Project Euler problem 18

triangle = []

# Parse triangle of numbers
f = open('triangle.txt')
line = f.readline()
while line != '':
    triangle.append(line.rstrip().split(' '))
    # Convert strings in row added to integers
    triangle[-1] = [int(x) for x in triangle[-1]]
    line = f.readline()

#print(triangle)

# Initialize lengthTo with default value 0
lengthTo = []
for row in triangle:
    lengthTo.append([])
    for i in row:
        lengthTo[-1].append(0)


row = 0
lengthTo[0][0] = triangle[0][0]
while row < len(triangle)-1:
    #print(lengthTo)
    i = 0
    while i < len(triangle[row]):
        #print('row =', row, '  i =', i)
        # left
        if lengthTo[row+1][i] <= lengthTo[row][i] + triangle[row+1][i]:
            lengthTo[row+1][i] = lengthTo[row][i] + triangle[row+1][i]

        # right
        if lengthTo[row+1][i+1] <= lengthTo[row][i] + triangle[row+1][i+1]:
            lengthTo[row+1][i+1] = lengthTo[row][i] + triangle[row+1][i+1]

        i += 1

    row += 1

print(max(lengthTo[-1]))

