def is_all_even(number):
	while number != 0:
		digit = number % 10
		if digit % 2 != 0:
			return False
		number = number // 10
	return True

def print_out():
	for number in range(1000, 3001, 2):
		if is_all_even(number):
			print(number, ",", end="\t")


print_out()
