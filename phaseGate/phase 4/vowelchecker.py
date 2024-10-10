

def vowel_conversion(letter):

	vowels = ['A','E','I','O','U','a','e','i','o','u']
	count = len(letter)
	check = False

	if count >1:
		print("input a single letter")
	else:
		for characters in range(len(vowels)):
			if letter == vowels[characters]:
				check = True
		print(check)
		
	
vowel_conversion("A")
	
	

	
			