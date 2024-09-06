def input_collection():
	first_number = float(input("input your first number"))
	second_number = float(input("input your second number"))
	third_number = float(input("input your third number"))
	return first_number, second_number, third_number


def display_sorted_numbers(first_number, second_number, third_number):
	largest = first_number
	smallest = first_number
	middle = 0
	
	if second_number > largest:
		largest = second_number
	if third_number > largest:
		largest = third_number

	if second_number < smallest:
		smallest = second_number
	if third_number < smallest:
		smallest = third_number

	if first_number != largest and first_number != smallest:
		middle = first_number
	elif second_number != largest and first_number != smallest:
		middle = second_number
	else: 
		middle = third_number 

	print(largest)
	print(middle)
	print (smallest)
	


display_sorted_numbers(*input_collection())