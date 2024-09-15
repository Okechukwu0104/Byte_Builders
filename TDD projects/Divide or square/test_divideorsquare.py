"""
test if divide_or_square function exist
check if a decimal hecking function is present too
confirm it works properly
..try with a number not divisible by 5
then with a number dividible by 5

make sure error is thrown if negative integer is inputed
and try a negative number too
"""


import unittest
import divideorsquare

class TestDivideorsquare(unittest.TestCase):
	def test_that_is_decimal_function_exists(self):
		divideorsquare.is_decimal(3)

	def test_that__divide_or_square_function_exists(self):
		divideorsquare.divide_or_square(3)


	def test_to_confirm_divide_or_square_function_works_properly(self):
		self.assertEqual(divideorsquare.divide_or_square(10),3.16)
		self.assertEqual(divideorsquare.divide_or_square(12),2)
		

	def test_to_check_if_error_pops_up_when_input_is_string(self):
		self.assertRaises(TypeError,divideorsquare,"cornflakes")
		

	def test_test_to_check_if_error_pops_up_when_input_is_decimal(self):
		self.assertRaises(TypeError,divideorsquare,(10.5))