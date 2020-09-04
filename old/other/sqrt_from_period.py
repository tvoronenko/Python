def sqrt_near(num):
	if num<0:
		raise ValueError("Wrong value")
	if num == 1:
		return 1
	for i in range(2,num/2):
		if i*i == num:
			return i
		elif i*i > num:
			return i-1



print(sqrt_near(9))
print(sqrt_near(124))