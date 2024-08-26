"""
1: tell the user to input the amount the client to borrow 
b) store the input as principal

2: tell the user to give a value for Annual interest rate
b) store the value as annual_interest_rate

3: tell the user to give a value for the Duration
b) store the value as Duration




do the calculation as follows: 0.05/12
b) save the result as monthly_interest_rate

do the calculation as follows: duration*12
b) save the result as duration_in_months


do the calculation as follows: 1 + monthly_interest_rate
b) save the result as one_plus_rate



4: do the calculation as follows: (principal*monthly_interest_rate)*(one_plus_rate)**duration_in_months
b) save the result as numerator_calculation

5: do the calculation as follows: ((one_plus_rate)** duration_in_months) -1
b) save the result as denominator_calculation

6: do the calculation as follows: numerator_calculation/denominator_calculation
b) save the result as monthly_payment

8: display the monthly_payment
"""

print("""
WELCOME! 
""")

principal = int(input("Enter the principal amount: "))
annual_interest_rate = int(input("Enter the Annual interest rate: "))
duration = int(input("Enter the duration in years: "))

monthly_interest_rate = 0.05/12
duration_in_months = duration*12
one_plus_rate= 1 + monthly_interest_rate

numerator_calculation = (principal*monthly_interest_rate)*(one_plus_rate)**duration_in_months

denominator_calculation = ((one_plus_rate)** duration_in_months) -1

monthly_payment = numerator_calculation / denominator_calculation

print("Your monthly payment is $" + str(round(monthly_payment, 2)))





