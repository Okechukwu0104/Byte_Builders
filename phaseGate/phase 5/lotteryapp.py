import random

user_input = input("input your 3 numbers: ")
count = len(user_input)
count = 0
in_built = []
while count !=3:
	value = random.randrange(1,10)
	in_built.insert(count, value)
	count +=1
print(in_built)
user = []

if count == 3:
	user_input = int(user_input)
	for digits in range(count):
		extract = abs(user_input % 10)			
		user.insert(0, extract)
		remain = user_input // 10
		user_input = remain
		
		
	exact_count = 0
	residual_count = 0

	for count in range(3):
		if user[count] == in_built[count]:
			exact_count += 1
		elif user[count] in in_built:
			residual_count += 1

			
	
	if exact_count == 3 :
		print("congrats..you have won $5000! (Highest prize)")
	
	elif exact_count == 2 or residual_count ==2 :
		print("congrats..you have won $4000! (2nd runner up)")
	elif exact_count == 1 or residual_count ==1 :
		print("congrats..you have won $1000! (3rd runner up)")

	else:
		print("you didnt win any prize")
	
	

	
else:
	print("You didn't input 3 numbers")