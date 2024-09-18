sum = 0
count = 0
while True:
	scores = int(input("input your scores "))
	if scores % 2 == 0:
		sum+=scores
	count+=1
	if count ==10:
		average = sum/count
		print("Total sum =",sum)
		print("Average =",average)
		break