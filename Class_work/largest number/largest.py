def get_maximum():
	number_one = int(input("input 1st numbers"))
	number_two = int(input("input 2nd numbers"))
	number_three = int(input("input 3rd numbers"))
	largest = 0
	if largest < number_one:
		largest = number_two
	elif largest <number_two:
		largest = number_three
	elif largest <number_three: 
		largest = number_one


	print(largest)

get_maximum()		