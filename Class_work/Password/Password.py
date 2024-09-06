'''
1) prompt the user to input a password
2) store the input as "user_input"
3) use len to determine the number of strings entered
'''

user_input = input ("give your password: ")
hash = len(user_input)
for star_output in range(hash):
	print("*", end= " ")
