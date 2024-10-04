list = [1,2,1,2,1,2,1,2,1,2,2,2] #1 2 


sum_of_even = 0
sum_of_odd = 0
multiply_at_p3 = 1
total = 0

def length(list):
	count = 0
	for numbers in list:
		count+=1
	
	return count


for digits in range(length(list)):
	if digits %2 == 0:
		sum_of_odd+= list[digits]

print("sum at odd indices",sum_of_odd)




for digits in range(length(list)):
	if digits %2 != 0:
		sum_of_even+= list[digits]

print("sum at even indices",sum_of_even)





for digits in range(length(list)):
	if digits % 3 == 0:
		multiply_at_p3*= list[digits]

print("multiplying at 3rd positions",multiply_at_p3)



for digits in range(length(list)):
	total+= list[digits]
	result = total / length(list)

print("Average =",round(result, 3))


