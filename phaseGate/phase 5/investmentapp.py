import math

investment = float(input("input an amount of investment: "))
years = float(input("number of years: "))
percentage = float(input("percentage per annum: "))
PERCENT = percentage/100


if years > 0 and percentage > 0 and investment > 0:
	years = round(years)
	print("we are using",years,"years (integer)")

	print("\nyear              ROI                   AAI")

	print("")
	for year in range(1,years+1):
		print(round(year), end="            \t")
		print(round(investment,3), end="            \t")
		roi = investment * PERCENT
		investment+=roi
		print(round(investment, 3) )
	
else:
	print("\nwrong input (a value is < 0)")
	
	
	
	
	