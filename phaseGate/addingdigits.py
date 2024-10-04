number = int(input("input a number "))
new_number = 0


while number != 0:
	if number < 1 and number >999:
		print("wrong input")

	extract = int(number % 10)
	new_number += extract
	remaining = int(number // 10)
	number = remaining
	
print(new_number)

	