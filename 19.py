#!/usr/bin/env python3
# Project Euler problem 19

sundaysOnFirst = 0

year = 1900
month = 1
firstOfMonth = 1
lastOfMonth = None

while year <= 2000:
    month = 1
    while month <= 12:
        daysInMonth = None
        if month in (4, 6, 9, 11): daysInMonth = 30
        if month in (1, 3, 5, 7, 8, 10, 12): daysInMonth = 31
        if month == 2: # February, need to account for leap years
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0: daysInMonth = 29
                    else: daysInMonth = 28
                else: daysInMonth = 29
            else: daysInMonth = 28

        if lastOfMonth != None:
            firstOfMonth = lastOfMonth + 1
            if firstOfMonth > 7:
                firstOfMonth = firstOfMonth - 7

            if (year != 1900) and (firstOfMonth == 7):
                sundaysOnFirst += 1

        lastOfMonth = (daysInMonth % 7) + firstOfMonth - 1
        if lastOfMonth > 7:
            lastOfMonth = lastOfMonth - 7

        month += 1

    year += 1

print(sundaysOnFirst)

