number_input = int(input("input a number: "))
array = []
first = 0
second = 1

print("")
for sequence in range(number_input-1):
	result = first + second
	array.insert(sequence,result)
	first = second
	second = result
	
	
print(array)
	
	
