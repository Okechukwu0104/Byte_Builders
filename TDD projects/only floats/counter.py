def only_floats(number1,number2):
	if not isinstance(number1,str) and not isinstance(number2,str):

		if number1 >0 and number2 >0:

			if isinstance(number1,float) and isinstance(number2,float):
				return 2

			elif isinstance(number1,float) or isinstance(number2,float):
				return 1
			
			else:
				return 0

		else:
			raise ValueError("negative number")
	else:
		raise TypeError("wrong input")


				