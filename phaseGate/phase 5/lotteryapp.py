import random
import sys

def lottery_app():
	balance = int(input("input your balance: "))
	bid = int(input("input stake amount (-1 to exit): "))
	while bid != -1:
		stake = bid

		user_input = input("input your 3 digits together: ")

		input_count = len(user_input)
		count = 0
		in_built = []

		user = []
		if balance < 0:
			print("insufficient balance")
		if input_count == 3:
			while count !=3:
				value = random.randrange(1,10)
				in_built.insert(count, value)
				count +=1
			print(in_built)
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
				print("congrats..you have won #5000! (Highest prize)")
				balance += 5000
				print("your balance is", balance)
		
			elif exact_count == 2 or residual_count ==2 :
				print("congrats..you have won #4000! (2nd runner up)")
				balance += 4000
				print("your balance is", balance)

			elif exact_count == 1 or residual_count ==1 :
				print("congrats..you have won #1000! (3rd runner up)")
				balance += 1000
				print("your balance is", balance)

			else:
				print("you didnt win any prize")
				balance -= stake
				print("your balance is",balance)
	

	
		else:
			print("You didn't input 3 numbers")


		if balance == 0 :
			break
	print("bye")

lottery_app()