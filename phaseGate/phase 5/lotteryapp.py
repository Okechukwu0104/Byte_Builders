user_input = input("input your 3 numbers")
count = len(user_input)
in_built = [3,3,0]
comma = ascii(",")
space = ascii(" ")

user = []

if count == 3:
	user_input = int(user_input)
	for digits in range(count):
		extract = abs(user_input % 10)			
		user.insert(count, extract)
		remain = user_input // 10
		user_input = remain
		
		
	counter = 3
	exact_count = 0
	residual_count = 0
	for numbers in range(counter):
		if user[numbers] == in_built[numbers]:
			exact_count+=1
		else:
			for count in range(counter):
				digit = user[count]
				for count in range(counter):
					if digit == in_built[count]:
						residual_count+=1
			
	
	if exact_count == 3:
		print("congrats..you have won $5000! (Highest prize)")
	
	elif exact_count == 2 or residual_count ==2 :
		print("congrats..you have won $4000! (2nd runner up)")
	else:
		print("congrats..you have won $1000! (3rd runner up)")

		
	
	

	
else:
	print("You didn't input 3 numbers")