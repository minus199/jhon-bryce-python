class Person:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender.upper()

    def __str__(self):
        return "Name: " + self.__name + " Gender: " + self.__gender


class Employee(Person):
    def __init__(self, name, gender, dept):
        super().__init__(name, gender)
        self.__dept = dept


me = Employee("Fred Bloggs", 'm', 'IT')
print(me)
