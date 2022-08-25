class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    #'salary' is the object from the salary class that we pass as an argument
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        #assign the salary object to 'obj_salary'
        self.obj_salary = salary #Aggregation
        
    def total_salary(self):
        return self.obj_salary.annual_salary()

#instantiating the salary class
salary = Salary(10000, 1200)
#pass the salary object to the constructor of the employee class
emp = Employee('John', 30, salary)
print(emp.total_salary())