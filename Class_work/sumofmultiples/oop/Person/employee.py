from person import Person


class Employee(Person):
    def __init__(self, name, age, dob, phone, street, city, state, id_number, email, level):
        super().__init__(name, age, dob, phone, street, city, state)
        self.__id_number = id_number
        self.__email = email
        self.__level = level

    def __str__(self):
        return f'''
        {super().__str__()}
        Id:{self.__id_number}
        Email:{self.__email}
        Level:{self.__level}
        
        '''
