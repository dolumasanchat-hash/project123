def func(lst):
	sum = 0
	
	for el in lst:
		sum += el
	
	return sum

tst = [1, 3, 6]
res = func(tst)
print(res) 