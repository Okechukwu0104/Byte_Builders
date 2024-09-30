number = int(input("input a number "))
new_number = 0

while number != 0:
	if not number >= 0 and number <=1000:
		print("wrong input")
		break
	extract = int(number % 10)
	new_number += extract
	remaining = int(number // 10)
	number = remaining
	
print(new_number)

	