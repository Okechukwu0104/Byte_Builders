vowels = ['A','E','I','O','U','a','e','i','o','u']
letter = "Adobe"
count = len(letter)
check = False


for characters in range(len(vowels)):
	if count >1:
		print("input a single letter")
	if letter == vowels[characters]:
		check = True
print(check)
		
	
		
	

	
			