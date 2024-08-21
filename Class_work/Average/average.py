"""
1) prompt the user to input the first number
2) store the number as "number_one"
3) prompt the user to input the second number
4) store the number as "number_two"
4) prompt the user to input the third number
5) store the number as "number_three"
6) calculate the sum : (number_one + number_two + number_three) 
7) store the result in variable "sum"
8) calculate sum / 38) store the result as "mean"
9) print the result for "mean"
"""

number_one = int(input ("input your 1st number"))
number_two = int(input("input your 2nd number"))
number_three = int(input("input your 2nd number"))

sum = (number_one + number_two + number_three)
mean = sum / 3

print("The mean: ", round(mean,2))

print("lets do another calculation")

