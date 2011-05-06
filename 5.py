c = 20

while True:
	c += 1
	i = 0
	print c
	while i <= 20:
		i += 1
		if c % i != 0:
			break
		else:
			if i == 20:
				print c
				exit()
