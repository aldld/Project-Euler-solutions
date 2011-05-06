#!/usr/bin/env python

def isPalindrome(s):
	s = str(s)
	if len(s) == 1:
		return True
	
	if s[0] == s[-1]:
		if len(s) == 2:
			return True
		if isPalindrome(s[1:-1]): # Recursion!
			return True

palindromes = []

for i in range(1000):
	for j in range(1000):
		if isPalindrome(i*j):
			palindromes.append(i*j)

print max(palindromes)
