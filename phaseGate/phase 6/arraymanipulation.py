array = [4,3,2,5,4,1]

product = 1
count = 0
def multiply_3rd_elements(array, product, count):
	
	for number in range(len(array)):
		count+=1
		if count %3 == 0:
			product *= array[number]
	print("multiplying 3rd elements:",product )	
multiply_3rd_elements(array, product, count)





def ascending_order(array):
	for number in range(len(array)):
		for num in range(len(array)-1):
			if array[num] > array[num+1]:
				temp = array[num]
				array[num] = array[num+1]
				array[num+1] = temp
	
	
	print(array)

ascending_order(array)


def ascending_order(array):
	for number in range(len(array)):
		for num in range(len(array)-1):
			if array[num] < array[num+1]:
				temp = array[num]
				array[num] = array[num+1]
				array[num+1] = temp
	
	
	print(array)

ascending_order(array)




def double_elements(array):

	for number in range(len(array)):
		array[number] *= array[number] 
	print("doubling the elements",array)

double_elements(array)






