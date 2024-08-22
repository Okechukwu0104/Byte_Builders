'''
score = int(input("input score: "))

if score <= 40:
	print("you got an F ")

if score <=60:
	print("you passed but not an A ")

if score > 75:
	print("you passed (A)")
'''



score = int(input("input your score"))
score_output = "failed"


if score >=40:
	score_output = "passed"
	print("well done...you ", score_output )

print("you ",score_output)