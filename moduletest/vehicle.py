class Vehicle:
    year=2020
    mpg=20
    speed=120
    
    def accelerate(self,value):
        return self.speed+value
    
    def brake(self,value):
        return self.speed-value
    
car1=Vehicle()

print('Displaying attributes')
print(car1.year)
print(car1.mpg)
print(car1.speed)
print()

print("Displaying method")
print(car1.accelerate(10))
print(car1.brake(30))

