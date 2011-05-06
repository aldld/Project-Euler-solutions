#!/usr/bin/env python
# Project Euler Problem 17

def numberToString(n):
    nString = str(n)[::-1]
    result = ''

    i = 0
    for digitStr in nString:
        digit = int(digitStr)
        if i == 1:
            if digit == 1:
                prevDigit = int(nString[i-1])
                if prevDigit == 0: result += 'ten'
                elif prevDigit == 1: result += 'eleven'
                elif prevDigit == 2: result += 'twelve'
                elif prevDigit == 3: result += 'thirteen'
                elif prevDigit == 4: result += 'fourteen'
                elif prevDigit == 5: result += 'fifteen'
                elif prevDigit == 6: result += 'sixteen'
                elif prevDigit == 7: result += 'seventeen'
                elif prevDigit == 8: result += 'eighteen'
                elif prevDigit == 9: result += 'nineteen'
            elif digit == 2: result += 'twenty'
            elif digit == 3: result += 'thirty'
            elif digit == 4: result += 'forty'
            elif digit == 5: result += 'fifty'
            elif digit == 6: result += 'sixty'
            elif digit == 7: result += 'seventy'
            elif digit == 8: result += 'eighty'
        else:
            if i == 2 and digit != 0:
                result += 'hundred'
                if nString[i-1] != 0 and nString[i-2] != 0:
                    result += 'and'
            elif i == 3: result += 'thousand'

            if digit == 1: result += 'one'
            elif digit == 2: result += 'two'
            elif digit == 3: result += 'three'
            elif digit == 4: result += 'four'
            elif digit == 5: result += 'five'
            elif digit == 6: result += 'six'
            elif digit == 7: result += 'seven'
            elif digit == 8: result += 'eight'
            elif digit == 9: result += 'nine'

        i += 1

    return result

total = 0
for i in range(1, 1000):
    print numberToString(i)
    total += len(numberToString(i))

print total

