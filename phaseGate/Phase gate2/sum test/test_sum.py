import unittest
import sum


class TestSum(unittest.TestCase):
	def test_that_sum_function_exist(self):
		sum.get_sum("3","4")


	def test_to_confirm_proper_functionality(self):
		self.assertEqual(sum.get_sum("10","10"),"20")
		self.assertEqual(sum.get_sum("10","-5"),"5")
		self.assertEqual(sum.get_sum("-5","-5"),"-10")


	def test_that_word_is_not_accepted_as_an_input(self):
		self.assertRaises(TypeError,sum,"phaseGate","wahala")

	
	def test_to_check_if_function_rejects_floaty_values(self):
		self.assertRaises(TypeError,sum,"5.5","7.3000")
