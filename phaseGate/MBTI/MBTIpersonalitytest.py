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
		answers = [None] * 20
		count = 0
		counter = 1
		
		while count != 20:
			print(f"{counter}. {self.optionsA[count]}     or      {self.optionsB[count]}")
			option = input().strip().upper()
			if option == "A":
				options.append(self.optionsA[count])
				answers[count] = option
				count += 1
				counter += 1
			elif option == "B":
				options.append(self.optionsB[count])
				answers[count] = option
				count += 1
				counter += 1
			else:
				print("Expected 'A' or 'B' as response. \nI know it's a mistake....Try again.\n")
		
		self.sort_and_display(options, answers, name)
		
	def sort_and_display(self, options, answers, name):
		# Implement the sorting and displaying logic here
		pass

if __name__ == "__main__":
	test = MBTIPersonalityTest()
	test.main()
