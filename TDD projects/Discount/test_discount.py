"""
1. check if the function exists 
2. check for accuracy of result 
3. returns an error if a negative discount or price is given 
4. returns error for strings and other unwanted data type 

"""

import unittest 
import discount

class TestDiscount(unittest.TestCase):
	
	def test_to_check_if_the_my_discount_function_exists(self):
		discount.my_discount(5000,10)


	def test_for_result_accuracy(self):
		self.assertEqual(discount.my_discount(150,15),127.5)						
		self.assertEqual(discount.my_discount(1000,50),500)
		self.assertEqual(discount.my_discount(1000,100),0)

	def test_to_check_if_error_popsup_for_string_entry(self):
		self.assertRaises(TypeError,discount,("cornflakes","milk"))
		self.assertRaises(TypeError,discount,("cornflakes",15))
		self.assertRaises(TypeError,discount,(500,"milk"))

	def test_to_check_for_negative_number_error(self):
		self.assertRaises(ValueError,discount.my_discount, 500,-15)
		self.assertRaises(ValueError,discount.my_discount, -500,15)
		self.assertRaises(ValueError,discount.my_discount, -500,-15)
		
		
		