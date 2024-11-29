class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        if isinstance(self.name, str):
            return self.name
        raise TypeError("Name should be a string")

    def get_age(self):
        if 0 < self.age <= 100:
            return self.age
        raise ValueError("age cannot be negative")

    def greet(self):
        return "Hello " + self.name
