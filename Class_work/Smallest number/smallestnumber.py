def get_minimum():
	number_one = int(input("input 1st numbers"))
	number_two = int(input("input 2nd numbers"))
	number_three = int(input("input 3rd numbers"))
	smallest = number_one
	if smallest > number_two:
		smallest = number_two
	elif smallest > number_three:
		smallest = number_three
	else:
		smallest = number_one


	print(smallest)

get_minimum()	