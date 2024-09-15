def get_transaction():
	balance = 0
	while True:
		choice = input("\nPick from the above options: ")
		match choice:
			case "1":
				amount = float(input("input an amount: ")) 
				balance+=amount
				print("\nDone !")
			case "2":
				amount = float(input("\ninput an amount: ")) 
				if amount <= balance or amount < 0:
					balance -= amount
					print("\nDone !")
				
				else:
					print("	   \nInsuffecient Funds")

			case "3":
				print("\nDetails\nbalance: #" , balance)
		
			case "4":
				print("Bye..")
				break

			case "5":
				options_display()
			case _:
				print("\ninvalid input...pls try again")



def options_display():
	print("""
		what do you want to do today?

		1. deposit ? 
		2. withdraw ?
		3. ckeck balance ?
		4. exit
		5. display menu

		""")

options_display()
get_transaction()


