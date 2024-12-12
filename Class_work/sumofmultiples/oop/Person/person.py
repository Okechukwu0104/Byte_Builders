from Address import Address


class Person:

    def __init__(self, name='anonymous', age='n/a', dob='dd/mm/yy', phone='00000000000', street='n/a', city='n/a',
                 state='n/a'):
        self.__set_name__(name)
        self.__age = age
        self.__dob = dob
        self.__phone = phone
        self.__address = Address(street, city, state)

    def __set_name__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def compare(self, obj):
        return obj.get_name == self.get_name() and obj.get_age == self.get_age()

    def greet(self):
        return "Hello " + self.__name

    def __str__(self):
        return f"""
        Name: {self.__name}
        Age: {self.__age}
        Dob: {self.__dob}
        Phone: {self.__phone}
        Address: {self.__address}
        """


person1 = Person("peter", 10, "10/3/2022", "08033271562", "H121", "Enugu", "Lagos state")
person2 = Person()
print(person1.compare(person2))
