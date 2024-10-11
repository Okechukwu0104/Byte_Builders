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
		
		


		exact_count = 0
		resudal_count = 0
		for numbers in range(3):
			if user[count] == in_built[count]:
				exact_count+=1

			else:
				for number in range(3):
					digit = user[count]
					for number in range(3):
						if digit == in_built[count]:
							residual_count+=1
			
	
		if exact_count == 3:
			print("congrats..you have won $5000! (Highest prize)")
	
		elif exact_count == 2 and residual_count ==2 :
			print("congrats..you have won $4000! (2nd runner up)")
		else:
			print("congrats..you have won $1000! (3rd runner up)")

		
	
	

	
else:
	print("You didn't input 3 numbers")