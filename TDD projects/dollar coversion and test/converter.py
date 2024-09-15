def get_converted_dollar(number):
	if isinstance(number, str):
		raise TypeError("Invalid type")
	RATE = 1550
	result = number * RATE
	return result