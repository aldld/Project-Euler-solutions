#!/usr/bin/env python
b = 0

def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False

	max = n**0.5 + 1
	i = 3

	while i <= max:
		if n % i == 0:
			return False
		i += 2
	
	return True

a = 0
c = 0
while True:
	a += 1
	if isPrime(a):
		if c == 10001:
			print a
			exit()
		c += 1
