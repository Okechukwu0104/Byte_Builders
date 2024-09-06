def main_header():
	while True:

		print("""
		:::::::::::::::::::::::::::::::::::::::::
			THE 12 DAYS OF CHRISTMAS
			Pick a Day from 1 - 12 
				
		  	or press 0 to exit
		::::::::::::::::::::::::::::::::::::::::::

		""")
		days = int(input())
		match days:
			case 1:
				day_one()
			case 2:
				day_two()
			case 3:
				day_three()
			case 4:
				day_four()
			case 5:
				day_five()
			case 6:
				day_six()
			case 7:
				day_seven()
			case 8:
				day_eight()
			case 9:
				day_nine()
			case 10:
				day_ten()
			case 11:
				day_eleven()
			case 12:
				day_twelve()
			case 0:
				print("Exiting >>>>>")
				break
			case _:
				print("Sorry...there is no", days,"th verse of the song\n\ntry again.. ")				
			

	

def day_one():
	print("""

	On the first day of Christmas my true love sent to me:

	-> A partridge in a pear tree


	""")
	
	



def day_two():
	print("""

	On the second day of Christmas my true love sent to me:

	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	



def day_three():
	print("""

	**On the third day of Christmas my true love sent to me**

	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	



def day_four():
	print("""

	**On the Fourth day of Christmas my true love sent to me**

	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	


def day_five():
	print("""

	**On the Fifth day of Christmas my true love sent to me**
	
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	


def day_six():
	print("""

	**On the Six day of Christmas my true love sent to me**

	-> six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	


def day_seven():
	print("""

	**On the Seven day of Christmas my true love sent to me**

	-> Seven swans a-swimming
	-> Six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	


def day_eight():
	print("""

	**On the Eight day of Christmas my true love sent to me**

	-> Eight maids a-milking
	-> Seven swans a-swimming
	-> Six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	

def day_nine():
	print("""

	**On the Ninth day of Christmas my true love sent to me**


	-> Nine ladies dancing
	-> Eight maids a-milking
	-> Seven swans a-swimming
	-> Six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	


def day_ten():
	print("""

	**On the Tenth day of Christmas my true love sent to me**

	-> Ten lords a-leaping
	-> Nine ladies dancing
	-> Eight maids a-milking
	-> Seven swans a-swimming
	-> Six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	

def day_eleven():
	print("""

	**On the Eleven day of Christmas my true love sent to me**

	-> Eleven pipers piping
	-> Ten lords a-leaping
	-> Nine ladies dancing
	-> Eight maids a-milking
	-> Seven swans a-swimming
	-> Six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	


def day_twelve():
	print("""

	**On the Twelfth day of Christmas my true love sent to me**

	-> Twelve drummers drumming
	-> Eleven pipers piping
	-> Ten lords a-leaping
	-> Nine ladies dancing
	-> Eight maids a-milking
	-> Seven swans a-swimming
	-> Six geese a-laying
	-> Five gold rings
	-> Four calling birds
	-> Three French hens,
	-> Two turtle doves,
	-> And a partridge in a pear tree.


	""")
	
	



main_header()