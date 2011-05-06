#!/usr/bin/env python3
# Project Euler problem 15

# Initialize grid, filled with -1's to indicate
# that no vertices have been touched yet
grid = []
x = 0
while x < 21:
    grid.append([])
    y = 0
    while y < 21:
        grid[x].append(-1)
        y += 1
    x += 1

x = 0
while x < 21:
    y = 0
    while y < 21:
        if (x == 0) or (y == 0):
            grid[x][y] = 1
        else:
            grid[x][y] = grid[x][y-1] + grid[x-1][y]
        y += 1
    x += 1

print(grid[20][20])

x = 0
y = 0
while x < 21:
    y = 0
    while y < 21:
        print(grid[x][y], end=' ')
        y += 1
    x += 1
    print()

