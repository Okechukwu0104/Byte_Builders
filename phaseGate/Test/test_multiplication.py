import unittest
import multiply


class TestMultiply(unittest.TestCase):
	def test_that_all_functions_exist(self):
		multiply.values(3,4)


	def test_to_check_if_returns_correct_result(self):
		self.assertEqual(multiply.values(3,4),12)
		self.assertEqual(multiply.values(-3,4),12)




