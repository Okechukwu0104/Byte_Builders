import unittest
import palindromicprime


class TestPalindromicprime(unittest.TestCase):
	def test_that_all_functions_exist(self):
		palindromicprime.if_palindromicprime(3)
		palindromicprime.palindrome(0)
		palindromicprime.prime(7)


	def test_to_confirm_prime_function_works(self):
		self.assertEqual(palindromicprime.prime(4),False)
		self.assertEqual(palindromicprime.prime(2),True)
		self.assertEqual(palindromicprime.prime(11),True)
		self.assertEqual(palindromicprime.prime(8),False)
		
		
	def test_if_prime_function_returns_error_for_strings(self):
		self.assertEqual(palindromicprime.palindrome(121),True)
		self.assertEqual(palindromicprime.palindrome(123),False)

	def test_if_palindromic_prime_works(self):
		self.assertEqual(palindromicprime.if_palindromicprime(92),False)
		self.assertEqual(palindromicprime.if_palindromicprime(131),True)