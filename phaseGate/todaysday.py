day = int(input("enter Todays day "))
future_day = int(input("Enter the number of days elapsed since Today "))


one = " Monday"
two = " Tuesday"
three = "wednesday"
four = "Thursday"
five = "Friday"
six = "Saturday"
seven = "Sunday"

result = day + future_day
week_count = 0
temp = week_count
year_count = 1

while result > 7:
	result = result -7
	week_count+=1
	

if temp >= 52:
	week_count -= 52
	year_count+=1
			
	
remain = abs(result % 7)

def future(future_day, result):
	
	count = 0
	while result > 7:
		result = result -7
		count+=1

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

future(future_day, result)


match day:

	case 1:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Monday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Monday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Monday and the future day is",value)
			

	case 2:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Tuesday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Tuesday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Tuesday and the future day is",value)

	case 3:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Wednesday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Wednesday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Wednesday and the future day is",value)

	case 4:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Thursday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Thursday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Thursday and the future day is",value)

	case 5:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Friday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Friday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Friday and the future day is",value)

	case 6:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Saturday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Saturday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Saturday and the future day is",value)

	case 7:
		value = future(future_day, result)
		if week_count >= 52:
			print("      Today is Sunday and the future day is",value,"\nThat is about", year_count,"year(s) ",week_count,"week(s) and",remain,"day(s) from now")
		elif week_count >1 and week_count <52:
			print("      Today is Sunday and the future day is",value,"\nApprox.",week_count,"week(s),",remain,"day(s),")
		else:
			print("      Today is Sunday and the future day is",value)


	case _:
		print("wrong input for day")


	


