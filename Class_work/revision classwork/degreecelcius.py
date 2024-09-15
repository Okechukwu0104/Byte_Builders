"""
..collect your degree input from the user in celcius

..perform a calculation to convert it to Fareheit:(9/5) * degreeInput + 32 and save the result as farenheit_Result

..print out the result


"""


celcius_input = float(input("input your degree celcius: "))

CONST_1 = 9/5
CONST_2 = 32
in_farenheit = (CONST_1 * celcius_input) + CONST_2

print(in_farenheit, "F")