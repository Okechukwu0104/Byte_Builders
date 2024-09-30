import unittest
import yas

class TestYas(unittest.TestCase):
	def test_to_check_if_all_functions_are_present(self):
		numbers = [1, 2, -5, 4, 5]
		new_array = [6,7,8,9,10]
		new_array2 = [4,4,2,1,3,]
		yas.largest(numbers)
		yas.reverse(numbers)
		yas.check(numbers,4)
		yas.odd_index(numbers)
		yas.even_index(numbers)
		yas.running_total(numbers)
		yas.is_palindrome("wahala")
		yas.sum(numbers)
		yas.sum2(new_array)
		yas.sum3(new_array)
		yas.concatenate(numbers,new_array)
		yas.alt_concatenate(numbers,new_array)


	def test_to_confirm_that_all_functions_are_working(self):
		numbers = [1, 2, 3, 4, 5]
		new_array = [6,7,8,9,10]
		new_array2 = [4,4,2,1,3,]
		self.assertEqual(yas.largest(numbers),5)
		self.assertEqual(yas.reverse(numbers),[5,4,3,2,1])
		self.assertEqual(yas.check(numbers,4),True)
		self.assertEqual(yas.odd_index(numbers),[2,4])
		self.assertEqual(yas.even_index(numbers),[1,3,5])
		self.assertEqual(yas.running_total(numbers),15)
		self.assertEqual(yas.is_palindrome("wahala"),False)
		self.assertEqual(yas.sum(numbers),15)
		self.assertEqual(yas.sum2(new_array),40)
		self.assertEqual(yas.sum3(new_array),40)
		self.assertEqual(yas.concatenate(numbers,new_array),[1, 2, 3, 4, 5, 6,7,8,9,10])
		self.assertEqual(yas.alt_concatenate(numbers,new_array),[1,6,2,7,3,8,4,9,5,10])


	
		
	def test_to_check_if_largest_function_runs_with_negative_numbers(self):
		self.assertEqual(yas.largest([1, -11, 3, -1, -2]),3)

	def test_to_confirm_largest_function_returns_error_on_string_input(self):
		self.assertRaises(TypeError, yas.largest,[1, "testing", 3, -1, -2])


	

	def test_to_confirm_reverse_function_returns_on_some_string_input(self): 
		self.assertEqual(yas.reverse(["two", "one", "testing"]),["testing","one","two"])
		self.assertEqual(yas.reverse(["two", 1, "testing"]),["testing",1,"two"])




		
	def test_to_confirm_odd_index_function_returns_error_for_string_input(self):
		self.assertRaises(TypeError, yas.odd_index,[1, "testing", 3, -1, -2])

	def test_to_chech_error_for_a_single_odd_index_element(self):
		self.assertRaises(ValueError,yas.odd_index,[4])





	def test_to_confirm_even_index_function_returns_error_for_string_input(self):
		self.assertRaises(TypeError, yas.even_index,[1, "testing", "wahala", -1, -2])
	
	def test_to_check_even_index_function(self):
		self.assertEqual(yas.even_index([4]),[4])


	def test_to_check_functionality_of_check_function(self):
		self.assertEqual(yas.check([4,-4],9),False)
		self.assertEqual(yas.check([],9),False)

	



	def test_to_confirm_running_total_function_returns_error_for_string_input(self):
		self.assertRaises(TypeError, yas.running_total,[1, "testing", "wahala", -1, -2])
	
	def test_to_check_correctness_of_running_total_function(self):
		self.assertEqual(yas.running_total([4]),4)

	def test_to_chech_correctness_of_running_total_function(self):
		self.assertEqual(yas.running_total([4,-4]),0)



	def test_to_
	














