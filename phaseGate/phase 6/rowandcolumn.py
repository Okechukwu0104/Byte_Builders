try:

	row = int(input("input the row "))
	collumn  = int(input("input your collumn "))
	if row >0 and collumn > 0:
		array = [[0]*row for _ in range(collumn)]

		for index in range(len(array)):
			for values in range(len(array[index])):
				print(f'{index*values:5}' , end = " ")

			print()
	else:
		print("input a positive number")
except:
	print("wrong input type")

	

