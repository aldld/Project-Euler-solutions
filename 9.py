#!/usr/bin/env python

a = 0
c = 0

while a <= 1000:
	a += 1
	b = 0

	while b <= 1000:
		b += 1
		c = a*a + b*b
		c = c**0.5

		if a + b + c == 1000:
			print a*b*c
			exit()
