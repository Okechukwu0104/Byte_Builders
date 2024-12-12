class Address:
    def __init__(self, street, city, state):
        self.__street = street
        self.__city = city
        self.__state = state

    def __str__(self):
        return f"""
                Street: {self.__street},
                City: {self.__city}
                State: {self.__state}
                """

person = Address("John", "Doe", "lagos state")
print(person)