

import unittest
import divideorsquare

class TestDivideorsquare(unittest.TestCase):

	def test_that__divide_or_square_function_exists(self):
		divideorsquare.divide_or_square(3)


	def test_to_confirm_divide_or_square_function_works_properly(self):
		self.assertEqual(divideorsquare.divide_or_square(10),3.16)
		self.assertEqual(divideorsquare.divide_or_square(12),2)
		

	def test_to_check_if_error_pops_up_when_input_is_string(self):
		self.assertRaises(TypeError,divideorsquare,"cornflakes")
		
