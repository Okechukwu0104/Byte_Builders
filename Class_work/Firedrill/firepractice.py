import random
def list_of_integers():
    num_array = []
    for i in range(0, 6):
        random_digit = random.randrange(1, 16)
        num_array.append(random_digit)
    return num_array
list_of_integers()

the_array = [4,3,2,1]
length = len(the_array)


def duplicate_elements(the_array,length):
    new_array = []
    for count in range(0, length):
        value = the_array[count]
        new_array.append(value)
    final_array = the_array + new_array
    return final_array
duplicate_elements(the_array,length)

numbers = [4, 3, 2, 1, 4, 3, 2, 1]
def duplicate_elimination(numbers,length):
    for count in numbers:
        if numbers[count] == numbers[count+(length+1)]:
            numbers.remove(numbers[count])
    return numbers
duplicate_elimination(numbers,length)
