class Employee:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x

john = Employee(2)
  
# setting the age using setter
john.set_age(19)
  
# retrieving age using getter
print(john.get_age())
print(john._age)