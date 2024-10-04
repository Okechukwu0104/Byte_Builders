
def get_sum(num1: str, num2: str):
	
	if isinstance(num1, str) and isinstance(num1, str):
		converted1 = int(num1) 
		converted2 = int(num2)
	else:
		raise TypeError("invalid Input")
	sum = converted1 + converted2

	result = str(sum)
	return result

