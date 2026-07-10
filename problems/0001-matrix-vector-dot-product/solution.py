def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	adotb=[]
	if len(a[0])==len(b):
		for row in a:
			temp=0
			for i in range(len(row)):
				temp+=row[i]*b[i]
			adotb.append(temp)
		return adotb
	else:
		return -1