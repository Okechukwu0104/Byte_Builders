

def get_futureinvvalue(investment_amount, yearly_interest_rate, years):
	
	if yearly_interest_rate < 0 or years < 0 or investment_amount < 0:
		raise TypeError("invalid number")

	elif isinstance(investment_amount, (str,)) or isinstance(yearly_interest_rate, (str,)) or isinstance(years, (str,)):
        	raise TypeError("Wrong type")
		
	else:

		monthly_interest_rate = float((yearly_interest_rate/100)/12)

		return round((investment_amount * (1 + monthly_interest_rate) ** (years*12)),3)

	