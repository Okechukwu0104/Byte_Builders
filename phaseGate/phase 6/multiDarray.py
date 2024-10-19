
"""
array1 = []
array2 = []
array3 = []
array4 = []
array5 = []

for _ in range(5):
	num = 0
	array1.insert(num,num)
	array2.insert(num,num)
	array3.insert(num,num)
	array4.insert(num,num)

array5.append(array1)
array5.append(array2)
array5.append(array3)
array5.append(array4)
print(array5)
print()

for numbers in range(5):
	print(array1[numbers] ,end = " ")
	print(array2[numbers],end = " ")
	print(array3[numbers],end = " ")
	print(array4[numbers],end = " \n")
"""

lst_zeros = [[0]*4 for _ in range(5)]
print(lst_zeros)



for row in range(len(lst_zeros)):
	for col in range(len(lst_zeros[row])):
		print(lst_zeros[row][col], end = " ")

	print()
