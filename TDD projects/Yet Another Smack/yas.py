def largest(numbers):
	if not isinstance(numbers, list):
		raise TypeError("Input should be a list")
	if not all(isinstance(number, (int, float)) for number in numbers):
		raise TypeError("All elements in the list should be numbers")
	
	largest = numbers[0]
	for number in numbers:
		if largest < number:
			largest = number
	return largest



def reverse(numbers):
	return numbers[::-1]

def check(numbers, check):
        return check in numbers

def odd_index(numbers):
	if len(numbers) < 2:
		raise ValueError("There is no odd element")
	if not isinstance(numbers, list):
		raise TypeError("Input should be a list")
	if not all(isinstance(number, (int, float)) for number in numbers):
		raise TypeError("All elements in the list should be numbers")
	
	return [numbers[i] for i in range(len(numbers)) if i % 2 != 0]


def even_index(numbers):
	if not isinstance(numbers, list):
		raise TypeError("Input should be a list")
	if not all(isinstance(number, (int, float)) for number in numbers):
		raise TypeError("All elements in the list should be numbers")
	return [numbers[i] for i in range(len(numbers)) if i % 2 == 0]

def running_total(numbers):
	if not isinstance(numbers, list):
		raise TypeError("Input should be a list")
	if not all(isinstance(number, (int, float)) for number in numbers):
		raise TypeError("All elements in the list should be numbers")
	return sum(numbers)

def is_palindrome(input_string):
        reversed_string = input_string[::-1]
        return input_string == reversed_string
	
def sum(numbers):
	sum = 0
	for number in numbers:
		sum+=number
	return sum	

def sum2(numbers):
        total = 0
        count = 0
        while count < len(numbers):
                total += numbers[count]
                count += 1
        return total

def sum3(numbers):
        total = 0
        count = 0
        while count < len(numbers):
                total += numbers[count]
                count += 1
        return total

def concatenate(numbers, new_array):
        return numbers + new_array


def alt_concatenate(numbers, new_array):
        result = []
        for i in range(max(len(numbers), len(new_array))):
                if i < len(numbers):
                        result.append(numbers[i])
                if i < len(new_array):
                        result.append(new_array[i])
        return result



def num_to_list(number):
	array = []
	count = 0
	while number != 0:
		extract = int(number/10)
		digit = int(number % 10)
		array.insert(count,digit)
		number = extract
		count+=1
	array.reverse()
	return array