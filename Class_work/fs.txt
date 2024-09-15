import unittest
import cube


class TestCube(unittest.TestCase):
	def test_that_cube_function_exist(self):
		cube.get_cube(3)


	def test_that_cube_function_returns_cube_result(self):
		self.assertEqual(cube.get_cube(10),1000)
		self.assertEqual(cube.get_cube(7),343)



		
	def test_that_cube_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError, cube.get_cube, -1)



	def test_function_that_function_returns_error_with_string_value(self):
		self.assertRaises(TypeError, cube.get_cube, "yea")







# assert Equal checks if the functions passed with a parameter passes the expected number   
# assertRaises is to catch errors and checkif it is true		