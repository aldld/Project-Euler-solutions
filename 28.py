#!/usr/bin/env python3
# Project Euler problem 28

def diagonalSum(n):
    # Check for an odd value of n
    if (n % 2 == 0): exit('diagonalSum requires an odd value for n')

    # Base case: n = 1
    if n == 1: return 1

    return diagonalSum(n-2) + 4*n*n - 6*n + 6

print(diagonalSum(1001))

