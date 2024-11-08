import math
import random


def list_of_integers():
    num_array = []
    for i in range(0, 17):
        random_digit = random.randrange(1, 16)
        num_array.append(random_digit)
    return num_array


the_array = list_of_integers()
length = len(the_array)
numbers = the_array * 2


def duplicate_elements(the_array, length):
    new_array = []
    for count in range(0, length):
        value = the_array[count]
        new_array.append(value)
    final_array = the_array + new_array
    return final_array


duplicate_elements(the_array, length)


def duplicate_elimination(numbers, length):
    for count in range(0, length):
        numbers.pop()
    return numbers


duplicate_elimination(numbers, length)


def sum_of_3rd_index(numbers):
    total = 0
    length = len(numbers)
    for digits in range(2, length, 3):
        total += int(numbers[digits])
    return total


sum_of_3rd_index(numbers)

def sum_of_3_indexes(numbers):
    ave = int(len(numbers) / 2)
    if len(numbers) % 2 == 0:
        ave = ave-1
        middle = int(numbers[ave] + numbers[ave+1])/2
    else:
        middle = numbers[math.ceil(ave)]
    print(middle)

    total = middle + numbers[0] + numbers[len(numbers)-1 ]
    return total


sum_of_3_indexes(numbers)
