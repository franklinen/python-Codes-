list = [2,3,4,5,3,78,5,6,10,2,4,8,9]
total = 0
for i in range(len(list)):
	list[i] = list[i] * 2
	total = total + list[i]
	
print total
