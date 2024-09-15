import math
import decimal

def is_decimal(number):
	return isinstance(number, decimal.Decimal)	

def divide_or_square(number):
	if is_decimal(number) or isinstance(number, str):
		raise TypeError("Invalid type")
		
	else:
		number = float(number)
		if number % 5 ==0:
			result = math.sqrt(number)
			return round(result,2)
		else:
			result = number % 5
			return result
		
	