"""
check for :
* if the function exists
1; accuracy of conversion
2; testing with boundry values 1 & 10,000,000
3; check if error pops when there is a wrong type of input(string)
4; check how well it is rounding up

"""

import unittest
import dollarconversion


class TestDollarConversion(unittest.TestCase):
	def test_that_dollar_conversion_function_exists(self):
		dollarconversion.get_converted_dollar(100)
	
	def test_to_check_if_converson_is_accurate(self):
		self.assertEqual(dollarconversion.get_converted_dollar(1),1550)
		self.assertEqual(dollarconversion.get_converted_dollar(100000),155000000)


	def test_to_check_if_error_popsup_when_string_is_inputed(self):
		self.assertRaises(TypeError, dollarconversion.get_converted_dollar,"dollars")

	
	def test_to_check_if_error_popsup_for_negative_money_input(self):
		self.assertRaises(ValueError, dollarconversion.get_converted_dollar,-100)
