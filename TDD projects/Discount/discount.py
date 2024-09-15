def my_discount(price, discount):
	if price < 0 or discount < 0:
		raise ValueError("invalid number")
	discount = discount/100
	deducted_amount = discount * price
	new_price = price - deducted_amount
	return new_price
		