
sum = 0
count = 0
while True:
	scores = int(input("input your scores "))
	if count%2 == 0:
		sum+=scores
	count+=1
	if count ==10:
		print("Total sum =",sum)
		break