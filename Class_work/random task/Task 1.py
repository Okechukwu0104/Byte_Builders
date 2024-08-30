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
"""

def bank():
    while True:
        print('''
		1...Deposit
		2...Withdrawal
		3...Balance details	
		3... exit
		''')
	
        user_amount_count = 0
        user_total_amount = 0

        user_choice = float(input("input your choice: "))
        match user_choice:
            case 1:
                amount_deposited =float(input("Enter amount to deposit (press -1 to exit): "))
                while (amount_deposited !=-1) :
                    user_total_amount += amount_deposited 

                    user_amount_count+=1
                    amount_deposited = float(input("press -1 or continue depositing: "))

                print ("Total:  #",user_total_amount, "\nyou deposited ", user_amount_count, " times")

	    case 2: 
                amount_withdrawn =float(input("Enter amount to withdraw (press -1 to exit): "))
		while (amount_withdrawn !=-1) :
		    user_total_amount -= amount_withdrawn
		    user_amount_count+=1

		    amount_withdrawn = float(input("press -1 or continue withdrawing: "))

		print ("Total left:  #",user_total_amount, "\nyou withdrew ", user_amount_count, " times")   			



bank()

	        
