#!/usr/bin/env python
# Project Euler problem 11

# Load the grid
grid = []
for line in open('grid.txt', 'r'):
    grid.append(line.split())

# Convert the grid to integers
for row in grid:
    i = 0
    while i < len(row):
        row[i] = int(row[i])
        i += 1

products = []
y = 0
while y < len(grid):
    x = 0
    while x < len(grid[y]):
        # Up
        if y >= 3:
            prod = grid[y][x] * grid[y-1][x] * grid[y-2][x] * grid[y-3][x]
            products.append(prod)
        
        # Down
        if y <= 16:
            prod = grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x]
            products.append(prod)

        # Left
        if x >= 3:
            prod = grid[y][x] * grid[y][x-1] * grid[y][x-2] * grid[y][x-3]
            products.append(prod)

        # Right
        if x <= 16:
            prod = grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3]
            products.append(prod)

        # Up Left
        if x >= 3 and y >= 3:
            prod = grid[y][x] * grid[y-1][x-1] * grid[y-2][x-2] * grid[y-3][x-3]
            products.append(prod)

        # Down Right
        if x <= 16 and y <= 16:
            prod = grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3]
            products.append(prod)
        
        # Up Right
        if x <= 16 and y >= 3:
            prod = grid[y][x] * grid[y-1][x+1] * grid[y-2][x+2] * grid[y-3][x+3]
            products.append(prod)

        # Down Left
        if x >= 3 and y <= 16:
            prod = grid[y][x] * grid[y+1][x-1] * grid[y+2][x-2] * grid[y+3][x-3]
            products.append(prod)
            
        x += 1

    y += 1

print max(products)
