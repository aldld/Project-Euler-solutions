#!/usr/bin/env python

def squares():
	a = []
	for i in range(1, 101):
		a.append(i*i)
	return a

print sum(squares()) - sum(range(1, 101))**2
print sum(range(1, 101))**2 - sum(squares())
