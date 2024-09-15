"""
1. display a message that shows the functions to choose from (Deposit and withdraw with an exit).
2. Ask for an option from the three
3. if it is to deposit (while), ask for the number to deposit 
4. add it continiously to the initial amount of 0 as long as the user keeps putting a valid number (except -1)
5) if the user inputs -1, you display the result of the addition
6. store the displayed number as "Total money"
7. for the withdrawal, you ask for how much needed 
8. then you subtract from the total amount from deposit 
9. as long as the user wants to, the user can withdraw but it should not exceed the total
10. when the user inputs -1, display the result still as total
add some other functionalities when these main things are done

"""

def bank():
	user_total_deposit = 0
	user_total_withdrawal = 0
	user_deposit_count = 0

	user_name = input("Before we Start..can we know your name?: ")
	user_title = input("Male or Female?: (input 'none' if neither) ")
	
	

	if(user_title == "male" or user_title == "Male"):
		user_title = "Mr"

	elif(user_title == "female" or user_title == "Female"):
		user_title = input("Single or Married?: ")

		if(user_title == "married" or user_title == "Married"):
			user_title = "Mrs"
		elif(user_title == "single" or user_title == "Single"):
			user_title = "Miss"
		else:
			print("Pls type appropriately")
			
	


	elif(user_title == "none" or user_title == "None"):
		user_title = input("Then what's your gender?: ")
		user_title = "Dear"
		
	else:
		print("Pls enter an appropriate input")
		
		
		
			
	
	while user_title == "Mr" or user_title == "Miss" or user_title == "Dear" :
		
		print("\nWelcome", user_title, user_name)
		print('''


		1...Deposit
		2...Withdrawal
		3...Balance / Transaction Details	
		4... exit

		''')
		
		
		user_choice = float(input("Input your choice: "))
		match user_choice:
			case 1:
				amount_deposited =float(input("Enter amount to deposit (press -1 to exit): "))
				while (amount_deposited !=-1) :
					user_total_deposit += amount_deposited 
	
					user_deposit_count+=1
					amount_deposited = float(input("press -1 or continue depositing: "))

				print ("Total:  #",user_total_deposit, "\n*",user_title, user_name,"deposited ", user_deposit_count, " times")
		

			case 2: 
				amount_withdrawn =float(input("Enter amount to withdraw (press -1 to exit): "))
				
				while (amount_withdrawn !=-1) :
					if (amount_withdrawn > user_total_deposit):
						print("      Insuffecient funds")
						break
						

					else:	
						user_total_deposit -= amount_withdrawn
						user_total_withdrawal+=1

						amount_withdrawn = float(input("press -1 or continue withdrawing: "))

					print("       Go to the Balance / Transaction details section to check your balance.")

                    
                    
			case 3:
				print(      user_title, user_name)
				print ("	Your Account Balance:  #", user_total_deposit)
				print("		You Deposited ",user_deposit_count , "times")
				print("		You Withdrew ", user_total_withdrawal, "times")

			case 4:
				print("Thank you for banking with us,", user_title, user_name )
				break
            			
			case _:
				print("invalid input.. pls try again")



bank()

	        
