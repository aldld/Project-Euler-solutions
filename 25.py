#!/usr/bin/env python3
# Project Euler problem 25

n = 2
fnmin1 = 1
fn = 1

while True:
    temp = fn
    fn += fnmin1
    fnmin1 = temp
    n += 1

    if len(str(fn)) >= 1000:
        print(n)
        break

