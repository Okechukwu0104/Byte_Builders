
sum = 0
count = 0
while True:
	scores = int(input("input your scores "))
	sum+=scores
	count+=1
	
	if count ==10:
		average = sum/count
		print("Total Average =",average)
		break