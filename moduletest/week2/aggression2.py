class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population
       
    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
       
    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()

country1 = Country("Little Island", 120)
p = Person("John", country1)
p.printDetails()
 
print()
#deletes the object p
del p
country1.printDetails()


#Phillips, D. (2015). Python 3 object-oriented programming. Packt Publishing Ltd. (page 11-14)