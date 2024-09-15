def palindrome(number):
	return str(number) == str(number)[::-1]

def prime(number):
	if number <= 1:
		raise ValueError("Wrong number input")
	if number == 2:
		return True
	for divisor in range(2, int(number ** 0.5) + 1): 
		if number % divisor == 0:
			return False
		else:
			return True
			

def if_palindromicprime(number):
	return palindrome(number) and prime(number)
	