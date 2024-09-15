"""
Ensure the function correctly calculates the future value for known inputs.
Example: future_investment_value(1000, 0.05 / 12, 10) should return approximately 1647.01.

Edge Cases:
Zero Investment: it returns 0.
Zero Interest Rate  0 interest returns the initial investment amount.
Zero Years: 0 years returns the initial investment amount.

Negative Investment, Negative Interest Rate, Negative Years, Large Values, Data Types(e.g., integers, floats), itsPerformance with a large number of years 

"""

import unittest
import futureinvvalue

class TestDivideorsquare(unittest.TestCase):
	def test_that_get_futureinvvalue_exists(self):
		futureinvvalue.get_futureinvvalue(1,1,1)
	
	def test_for_accurate_result_for_small_and_large_number_entries(self):
		self.assertEqual(futureinvvalue.get_futureinvvalue(1000, 5, 10),1647.009)
		self.assertEqual(futureinvvalue.get_futureinvvalue(2500, 4.5, 8),3580.912)

	def test_to_check_if_error_pops_up_when_input_is_string(self):
		self.assertRaises(TypeError,futureinvvalue,"cornflakes")	
	
	def test_to_check_possible_edge_cases(self):
		self.assertEqual(futureinvvalue.get_futureinvvalue(0, 5, 10),0)
		self.assertEqual(futureinvvalue.get_futureinvvalue(1000, 0, 10),1000)
		self.assertEqual(futureinvvalue.get_futureinvvalue(1000, 5, 0),1000)
		
	def test_if_error_popsup_for_negative_values_input(self):
		self.assertRaises(TypeError, futureinvvalue, (-1000, 5, 10))
		self.assertRaises(TypeError, futureinvvalue, (1000, -5, 10))
		self.assertRaises(TypeError, futureinvvalue, (1000, 5, -10))

		