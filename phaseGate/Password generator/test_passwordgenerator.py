import unittest
import passwordgenerator


class Testpasswordgenerator(unittest.TestCase):
	def test_to_check_if_password_generator_is_present(self):
		passwordgenerator.generate_password()
		passwordgenerator.gen()
		passwordgenerator.character_checker()
		passwordgenerator.symbol_checker()
		passwordgenerator.length_check(18)


	def test_to_check_if_function_contains_letters_capital_and_lowercase(self):
		self.assertEqual(passwordgenerator.character_checker(),True)


	def test_to_check_if_function_contains_symbols(self):
		self.assertEqual(passwordgenerator.symbol_checker(),True)

	def test_to_check_if_function_contains_symbols(self):
		self.assertEqual(passwordgenerator.length_check(16),True)


	def test_to_check_if_function_contains_digits(self):
		self.assertEqual(passwordgenerator.digit_checker(),True)