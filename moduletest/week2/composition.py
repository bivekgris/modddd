class Salary:
    #salary class constructor
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    #salary class method
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    #employee class constructor
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        #creating object of salary class
        self.obj_salary = Salary(pay, bonus) #Composition
    
    #employee class method    
    def total_salary(self):
        #calling annual_salary() method of salary class
        return self.obj_salary.annual_salary()

#creating object of employee class    
emp = Employee('John', 30, 10000, 1200)
#calling total_salary() of employee class
print(emp.total_salary())