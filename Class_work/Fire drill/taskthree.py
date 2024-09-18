count = 0
sum = 0

while count != 10:
	scores = int(input("input 10 scores "))
	sum +=scores
	count+=1
	
average = sum/count
print("sum =", sum)
print("average =", average)
	