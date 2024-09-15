def get_cube(number):
	if number < 0:
		raise ValueError("Invalid Number")
	return number **3