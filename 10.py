#!/usr/bin/env python

def isPrime(x):
	if x == 2:
		return True
	if x % 2 == 0:
		return False

	max = x**0.5 + 1
	i = 3

	while i <= max:
		if x % i == 0:
			return False
		i += 2
	
	return True

j = 3
p = 2

while j <= 2000000:
	j += 2
	if isPrime(j):
		if j >= 2000000:
			print p
			exit()
		else:
			p += j

