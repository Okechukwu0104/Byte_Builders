import random
import creditcardvalidator

def card_generator_function():
    counter = 0
    the_13 = 0
    illegit = True
    while counter != 13:
        digits = random.randint(0, 9)
        the_13 = the_13 * 10 + digits
        counter += 1

    while illegit:
        if creditcardvalidator.is_valid(the_13):
            illegit = False
            return "777" + str(the_13)

