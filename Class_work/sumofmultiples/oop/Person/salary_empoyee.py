from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name='anonymous', age='n/a', dob='dd/mm/yy', phone='00000000000', street='n/a', city='n/a',
                 state='n/a', id_number='000000', email='johndoe@gmail.com', level='0', salary='0'):

        super().__init__(name, age, dob, phone, street, city, state, id_number, email, level)
        self.__salary = salary

    def __str__(self):
        return f"""
        {super().__str__()}
        Salary: {self.__salary}
        """


s1 = SalaryEmployee("Peter", 10, "23/2/2004", "09059947033", "H121", "Ikeja", "Lagos",
                    "18/sci03/007", "Okechukwupeter10@gmail.com", "CTO", "20B")

print(s1)
