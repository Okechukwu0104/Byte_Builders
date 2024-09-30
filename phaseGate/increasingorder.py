count = 1

largest = float('-inf')
middle = float('-inf')
small = float('inf')

while count <= 3:
	number = int(input("Enter your number"))

	if number > largest:
		middle = largest
		largest = number
	elif number > middle:
		middle = number
    
	if number < small:
		small = number
    

	count += 1

print(small, middle, largest)
