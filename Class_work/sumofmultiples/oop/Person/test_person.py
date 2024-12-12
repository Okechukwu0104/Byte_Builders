import unittest
from person import Person


class PersonCase(unittest.TestCase):
    def test_the_Name_function(self):
        new_person = Person("peter", 10)
        self.assertEqual(new_person.greet(), "Hello peter")

    def test_that_get_age_returns_the_age(self):
        new_person = Person("peter", 10)
        self.assertEqual(new_person.get_age(), 10)

    def test_that_function_throws_error_on_negative_age(self):
        new_person = Person("peter", -10)
        self.assertRaises(ValueError, new_person.get_age)

    def test_that_function_throws_error_on_integer_as_name(self):
        new_person = Person(10,100)
        self.assertRaises(TypeError, new_person.get_name)


    def test_that_age_shouldnt_exceed_max_age(self):
        new_person = Person("peter", 110)
        self.assertRaises(ValueError, new_person.get_age)


if __name__ == '__main__':
    unittest.main()
