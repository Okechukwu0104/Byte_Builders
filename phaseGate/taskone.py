import random


number1 = random.randrange(10) 
number2 = random.randrange(10) 

result = number1 + number2

print("what is the sum of",number1,"and",number2,"?")
prompt = int(input())

print(prompt == result)
	