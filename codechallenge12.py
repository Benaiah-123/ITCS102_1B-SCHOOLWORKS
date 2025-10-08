for i in range(1, 10, 1):
	for z in range(10, i, -1):
		print(" ", end = " ")
	for p in range(i, 0, -1):
		print(p, end = " ")
	for j in range(2, i + 1, 1):
		print(j, end = " ")
	print()

