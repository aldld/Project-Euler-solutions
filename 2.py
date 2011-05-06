#!/usr/bin/env python

def fib():
	a = 0
	b = 1
	d = []

	while True:
		c = b
		b = a + b
		a = c
		
		if b >= 4000001:
			break
		else:
			if b % 2 == 0:
				d.append(b)
	return d

foo = 0
for i in fib():
	foo += i

print foo
