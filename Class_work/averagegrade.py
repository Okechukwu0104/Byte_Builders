def collection():
	counter = 0
	scores = 0
	count2 = 0
	score_input = float(input("input your student's scores / press -1 to end: "))
	while score_input != -1 :
		score_input = float(input("press -1 anytime to end: "))
		if score_input >=0 and score_input <= 100:
			scores += score_input
			counter+=1
		else:
			count2+=1

	
	average = scores / counter
	print("The average score is:", average)
	print(count2-1,"scores were not added")
		
	

collection()