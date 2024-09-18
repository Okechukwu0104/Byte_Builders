
sum = 0
count = 0
while True:
	scores = int(input("input your scores "))
	if scores >=0 and scores < 101:
		sum+=scores
	count+=1
	if count ==10:
		average = sum / count
		print("Average =",average)
		break