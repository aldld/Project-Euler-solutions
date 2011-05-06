#!/usr/bin/env python3
# Project Euler problem 24

a = range(10)

i = 1
while i <= 999999:
    # Find the largest index k s.t. a[k] < a[k+1]
    j = 0
    k = j
    while j < len(a) - 1:
        if a[j] < a[j+1]:
            k = j
        j += 1

    # Find the largest index l s.t. a[k] < a[l]
    j = 0
    l = 0
    while j < len(a):
        if a[k] < a[j]:
            l = j
        j += 1

    # Swap a[k] with a[l]
    a[k], a[l] = a[l], a[k]

    # Reverse sequence from a[k+1] to end
    a[(k+1):len(a)] = a[(k+1):len(a)][::-1]

    i += 1

print(a)

