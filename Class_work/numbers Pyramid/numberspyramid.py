view = int(input("input a number: "))
for first in range(1,view):
	for second in range(first,view):
		print(second,end = " ")

	print ()

print()
print()

for first in range(view, 0,-1):
	for second in range(view, 0,-1):
		print(first,end = " ")



'''
	print(f'{}x{}={}')
	placehodler in python
'''