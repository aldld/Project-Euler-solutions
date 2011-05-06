#!/usr/bin/env python3
# Trying to implement merge sort

from math import floor

def merge(a, b):
    result = []
    while (len(a) > 0) or (len(b) > 0):
        if (len(a) > 0) and (len(b) > 0):
            if a[0] <= b[0]:
                result.append(a[0])
                del a[0]
            else:
                result.append(b[0])
                del b[0]
        elif len(a) > 0:
            result.append(a[0])
            del a[0]
        elif len(b) > 0:
            result.append(b[0])
            del b[0]

    return result

def mergeSort(m):
    if len(m) <= 1: return m

    middle = int(floor(len(m)/2))
    a = m[0:middle]
    b = m[middle:len(m)]

    a = mergeSort(a)
    b = mergeSort(b)
    result = merge(a, b)

    return result

