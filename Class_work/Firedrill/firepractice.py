import math


def list_of_integers():
    num_array = list(range(1, 16))
    for digit in num_array:
        if digit < 0:
            raise ValueError('must be a positive number')
    return num_array


the_array = list_of_integers()
length = len(the_array)
numbers = the_array * 2


def duplicate_elements(the_array, length):
    new_array = []
    for count in range(0, length):
        if not isinstance(the_array[count], int):
            raise TypeError('Invalid type')
        if the_array[count] < 0:
            raise ValueError('must be a positive number')

        value = the_array[count]
        new_array.append(value)
    final_array = the_array + new_array
    return final_array


duplicate_elements(the_array, length)


def duplicate_elimination(numbers, length):
    for count in range(0, length):
        if not isinstance(numbers[count], int):
            raise TypeError('Invalid type')
        if numbers[count] < 0:
            raise ValueError('must be a positive number')
        numbers.pop()
    return numbers


duplicate_elimination(numbers, length)


def sum_of_3rd_index(numbers):
    total = 0
    length = len(numbers)
    for digits in range(2, length, 3):
        if not isinstance(numbers[digits], int):
            raise TypeError('Invalid type')
        elif numbers[digits] < 0:
            raise ValueError('must be a positive number')
        total += int(numbers[digits])
    return total


sum_of_3rd_index(numbers)


def sum_of_3_indexes(numbers):
    for count in range(0, len(numbers)):
        if not isinstance(numbers[count], int):
            raise TypeError('Invalid type')
        if numbers[count] < 0:
            raise TypeError('must be a positive number')

    ave = int(len(numbers) / 2)
    if len(numbers) % 2 == 0:
        ave = ave - 1
        middle = int(numbers[ave] + numbers[ave + 1]) / 2
    else:
        middle = numbers[math.ceil(ave)]
    total = middle + numbers[0] + numbers[len(numbers) - 1]
    return total


sum_of_3_indexes(numbers)
