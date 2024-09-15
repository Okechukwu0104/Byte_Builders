"""
check if only_floats exist
check if the results are correct
check if error pops up when a negative number and string is passed into the function 


"""

import unittest
import counter

class TestCounter(unittest.TestCase):
	def test_to_check_if_only_floats_function_exists(self):
		counter.only_floats(7,7)


	def test_to_check_accuracy_of_result(self):
		self.assertEqual(counter.only_floats(12.1,23),1)
		self.assertEqual(counter.only_floats(12,239.8),1)
		self.assertEqual(counter.only_floats(12.5,23.5),2)

	def test_to_check_if_eror_pops_up_for_negative_numbers_and_strings(self):
		self.assertRaises(TypeError,counter,(12.1,"cornflakes"))
		self.assertRaises(TypeError,counter,("milk",44))

		self.assertRaises(TypeError,counter,("milk or milo","cornFlakes"))

		self.assertRaises(TypeError,counter,("milk",-44))

		self.assertRaises(ValueError,counter.only_floats,-121,-44)	
	
	