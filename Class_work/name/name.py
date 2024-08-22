"""
prompt the user to enter name
store the input as name_input
store it as input_type
if the input_type is a string; print "your name is "name_input"
if the userInput is not a string, print "that is an invalid input"
"""

name_input = input("Input your programming languagename ") 



'''

name_input = input("what is your name ")
if name_input  :
	print("Your name is ", name_input)

else :
	print("that is an invalid input")
'''



match name_input:
	case "java": 
		print ("ok")

	case "python":
		print ("this is the second option")
	case "javascript":
		print ("ok..thats fine")
	case _: 
		print ("this is invalid")
