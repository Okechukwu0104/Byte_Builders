day = int(input("enter todays day "))
future_day = int(input("Enter the number of days elapsed since today "))


one = " Monday"
two = " Tuesday"
three = "wednesday"
four = "Thursday"
five = "Friday"
six = "Saturday"
seven = "Sunday"

def future(future_day):
	result = day + future_day

	if result ==1:
		return(one)

	if result ==2:
		return(two)

	if result ==3:
		return(three)

	if result ==4:
		return(four)

	if result ==5:
		return(five)

	if result ==6:
		return(six)

	if result ==7:
		return(seven)

future(future_day)


match day:

	case 1:
		value = future(future_day)
		print("today is Monday and the future day is",value)

	case 2:
		value = future(future_day)
		print("today is Tuesday and the future day is",value)

	case 3:
		value = future(future_day)
		print("today is Wednesday and the future day is",value)

	case 4:
		value = future(future_day)
		print("today is Thursday and the future day is",value)

	case 5:
		value = future(future_day)
		print("today is Friday and the future day is",value)

	case 6:
		value = future(future_day)
		print("today is Saturday and the future day is",value)

	case 7:
		value = future(future_day)
		print("today is Sunday and the future day is",value)





	


