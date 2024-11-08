import unittest
import firepractice


class Testfirepractice(unittest.TestCase):
    def test_for_functions_existence(self):
        firepractice.list_of_integers()

    def test_for_random_integer_array(self):
        random = firepractice.list_of_integers()
        self.assertEqual(random, random)

    def test_to_check_if_elements_are_duplicated(self):
        the_array = [4, 3, 2, 1]
        expected = [4, 3, 2, 1, 4, 3, 2, 1]
        result = firepractice.duplicate_elements(the_array)
        self.assertEqual(expected, result)

    def test_if_duplicate_elimination_succeds(self):
        numbers = [4, 3, 2, 1, 4, 3, 2, 1]
        expected = [4, 3, 2, 1]
        length = 8
        result = firepractice.duplicate_elimination(numbers, length)
        self.assertEqual(expected, result)
