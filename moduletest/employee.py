class Employee:
    name='Bivek'
    age='28'
    Salary=1500
    
    def bonus(self,bonus):
        return self.Salary+bonus
    
    def fined(self,fine):
        return self.Salary-fine
    
em1=Employee()
print(em1.name)
print(em1.age)
print(em1.Salary)

print(em1.bonus(300))
print(em1.fined(100))