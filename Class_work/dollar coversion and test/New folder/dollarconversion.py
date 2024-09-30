def get_converted_dollar(number):
	if isinstance(number, str):
		raise TypeError("Invalid type")
	if number < 0:
		raise ValueError("wrong number")
	RATE = 1550
	result = round( number * RATE )
	return result