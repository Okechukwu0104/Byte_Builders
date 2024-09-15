"""
1.. make the liter of fuel(i.e #855) a constant variable
2.. ask user for his budget(how much he wants to buy)
3.. divide the users budget by the standard price of fuel(#855)to get the liters that can be bought
4..print out the liters that can be bought 

"""

FUEL_PRICE = 855
user_budget = float(input("input your fuel Budget"))
liters_purchasable = user_budget / FUEL_PRICE
print(liters_purchasable)

