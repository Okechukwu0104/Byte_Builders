def check_card_type(number, length):
	if length >=13 and length<=16:
		digit = number[0]
		digit2 = number[1] 
        
		if digit == '4':
			return "Visa"
		elif digit == '5':
			return "Mastercard"
		elif digit == '6':
			return "Discover"
		elif digit == '3' and digit2 == '7':
			return "American Express"
	return "Invalid card"




def is_valid(credit_card_no):
	number = int(credit_card_no)
	card_no = []
	while number != 0:
		extract = number % 10
		card_no.append(extract)
		number //= 10
    
	sum = 0
	for count, value in enumerate(card_no):
		if count % 2 != 0:
			value *= 2
			if value > 9:
				value = (value // 10) + (value % 10)
		sum += value
    
	return "valid" if sum % 10 == 0 else "invalid"



try:
	credit_card_no = input("Hello, Kindly enter card details to verify: ")
	length = len(credit_card_no) 
  
	card_type = check_card_type(credit_card_no, length)
	validity = is_valid(credit_card_no)
    
	print(f"""
	Credit Card Type: {card_type}
	Credit Card Number: {credit_card_no}
	Credit card Digit Length: {length}
	Credit card Validity Status: {validity}
	    """)

except:
	print("You must've inputed a non-intger somewere...")    







