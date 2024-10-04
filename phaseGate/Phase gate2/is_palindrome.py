
def reverse(number):
	new = 0
	while number != 0:
		extract = number % 10
		remain = number // 10
		new = new*10 + extract
		number = remain
		
		
	return new



def is_palindrome(number):

	if reverse(number) == number:
		print("its a palindrome")
	else:
		print("its not a palindrome")




is_palindrome(21212)