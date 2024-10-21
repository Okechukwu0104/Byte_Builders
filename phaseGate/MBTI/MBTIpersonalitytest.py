class MBTIPersonalityTest:
	
	def __init__(self):
		self.optionsA = [
			"expend energy, enjoy groups", "Interpret literally", "logical, thinking, questioning", 
			"organized, orderly", "more outgoing, think out loud", "practical, realistic, experiential", 
			"candid, straightforward, frank", "plan, schedule", "seek many tasks, public activities, interaction with others", 
			"standard, usual, conventional", "firm, tend to criticize, hold the line", "regulated, structured", 
			"external, communicative, express yourself", "focus on here-and-now", "tough-minded, just", 
			"preparation, plan ahead", "active, initiate", "facts, things, what is, ideas", 
			"matter of fact, issue-oriented", "control, govern"
		]
		
		self.optionsB = [
			"conserve energy, enjoy one-on-one", "look for meaning and possibilities", "empathetic, feeling, accommodating", 
			"flexible, adaptable", "more reserved, think to yourself", "imaginative, innovative, theoretical", 
			"tactful, kind, encouraging", "unplanned, spontaneous", "seek private, solitary activities with quiet to concentrate", 
			"different, novel, unique", "gentle, tend to appreciate, conciliate", "easy-going, live and let live", 
			"internal, reticent, keep to yourself", "look to the future, global perspective, big picture", 
			"tender-hearted, merciful", "go with the flow, adapt as you go", "reflective, deliberate", 
			"ideas, dreams, what could be, philosophical", "sensitive, people-oriented, compassionate", "latitude, freedom"
		]
		
	def main(self):
		name = input("What is your Name? : ")
		name = name.capitalize()
		self.questions(name)
		
	def questions(self, name):
		print(f"You're Welcome {name}.\nPlease answer these 20 set of questions ('A' or 'B')\n")
		
		options = []
		answers = [None] 
		count = 0
		counter = 1
		
		while count != 20:
			print(f"{counter}. {self.optionsA[count]}     or      {self.optionsB[count]}")
			option = input().strip().upper()
			if option == "A":
				options.append(self.optionsA[count])
				answers.append( option)
				count += 1
				counter += 1
			elif option == "B":
				options.append(self.optionsB[count])
				answers.append( option)
				count += 1
				counter += 1
			else:
				print("Expected 'A' or 'B' as response. \nI know it's a mistake....Try again.\n")
		
		self.sort_and_display(options, answers, name)
		
	def sort_and_display(self, options, answers, name):
		options_array = [[None for _ in range(5)] for _ in range(4)]
		answers_array = [[None for _ in range(5)] for _ in range(4)]
		personality_trait = ""
		counter1 = 0

		for count1 in range(5):
			for count2 in range(4):
				options_array[count2][count1] = options[counter1]
				answers_array[count2][count1] = answers[counter1]
				counter1 += 1

		versus_display = ["Extraverted (E) vs Introverted (I)","Sensing (S) vs Intuitive (N)","Thinking (T) vs Feeling (F)","Judging (J) vs Perceptive (P)"]

    
		print(f"\nHello {name}, You selected: \n\n\n")

    
		for count1 in range(4):
        
		
			a_count = 0
			b_count = 0
			print(f"       -> {versus_display[count1]}\n")
        
			for count2 in range(5):
            
				print(f"{answers_array[count1][count2]}. {options_array[count1][count2]}")
				if answers_array[count1][count2] == "a":
					a_count += 1
				else:
               
					b_count += 1
            	
			print()

        
			output = f"""
        
			Number of 'A' selected: {a_count}
			number of 'B' selected: {b_count}
        
			"""
			print(output)
		
			print()

        
			if a_count > b_count and count1 == 0:
				personality_trait += "E"
        
			elif a_count < b_count and count1 == 0:
				personality_trait += "I"

        
			if a_count > b_count and count1 == 1:
				personality_trait += "S"
        
			elif a_count < b_count and count1 == 1:
				personality_trait += "N"

        
			if a_count > b_count and count1 == 2:
				personality_trait += "T"
        
			elif a_count < b_count and count1 == 2:
				personality_trait += "F"

        
			if a_count > b_count and count1 == 3:
				personality_trait += "J"
        
			elif a_count < b_count and count1 == 3:
				personality_trait += "P"

    
		print(f"personalityTrait: {personality_trait}\n\n")
		personality_brief(personality_trait)



	def personality_brief(trait):
		print(f"Personality Brief for {trait}")


if __name__ == "__main__":
	test = MBTIPersonalityTest()
	test.main()
