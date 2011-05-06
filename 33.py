#!/usr/bin/env python3
# Project Euler problem 33

curious = []

for numerator in range(10, 100):
    for denominator in range(numerator+1, 100):
        ratio = numerator/denominator
        if str(numerator)[0] == str(denominator)[1]:
            if int(str(numerator)[1])/int(str(denominator)[0]) == ratio:
                curious.append([numerator, denominator])
        if str(numerator)[1] == str(denominator)[0]:
            if int(str(denominator)[1]) != 0:
                if int(str(numerator)[0])/int(str(denominator)[1]) == ratio:
                    curious.append([numerator, denominator])


