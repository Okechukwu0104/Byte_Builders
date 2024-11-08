import unittest
import firepractice


class Testfirepractice(unittest.TestCase):
    def test_for_functions_existence(self):
        firepractice.list_of_integers()

    def test_for_random_integer_array(self):
        random = firepractice.list_of_integers()
        self.assertEqual(random, random)

    def test_to_check_if_elements_are_duplicated(self):
        the_array = firepractice.list_of_integers()
        expected = the_array * 2
        length = len(the_array)
        result = firepractice.duplicate_elements(the_array, length)
        self.assertEqual(expected, result)

    def test_if_duplicate_elimination_works(self):
        expected = firepractice.list_of_integers()
        numbers = expected * 2
        length = len(expected)
        result = firepractice.duplicate_elimination(numbers, length)
        self.assertEqual(expected, result)

    def test_that_every_3rd_element_is_added(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        result = 9
        expected = firepractice.sum_of_3rd_index(numbers)
        self.assertEqual(expected, result)

    def test_to_sum_first_middle_last_elements(self):
        numbers = [1, 2, 2, 6]
        result = firepractice.sum_of_3_indexes(numbers)
        expected = 9.0
        self.assertEqual(expected, result)

        numbers = [1, 2, 4, 5, 6]
        result = firepractice.sum_of_3_indexes(numbers)
        expected = 11
        self.assertEqual(expected, result)
