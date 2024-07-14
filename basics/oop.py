class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        return f"The {self.make} {self.model}'s engine has started."

toyota = Vehicle("Toyota", "Corolla", 2020)
honda = Vehicle("Honda", "CRV", 2023)

print(toyota.start_engine())
print(honda.start_engine())

## Inheritance

class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    def print_info(self):
        return f"Info: {self.name} {self.lastname}, {self.age} years old."

class Employee(Person):
    def __init__(self, name, lastname, age, salary):
        super().__init__(name, lastname, age)
        self.salary = salary

    def print_info(self):
        print(f"Info: {self.name} {self.lastname}, {self.age} years old. Earning {self.salary} a year")

    def increase_salary(self, percentage):
        self.salary = self.salary + ((self.salary * percentage) // 100)


employee = Employee("Jeffrey", "Almanzar", 27, 130000)
employee.print_info()
employee.increase_salary(40)
employee.print_info()