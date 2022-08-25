class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def Perimeter(self):
        return 2*(self.length+self.width)
    
    def Area(self):
        return self.length*self.width
    
    def display(self):
        return (f'Length: {self.length}, Width: {self.width}, Perimeter {Rectangle.Perimeter(self)} and Area {Rectangle.Area(self)}')
    
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height=height
    
    def Volume(self):
        return self.length*self.width*self.height
    
myRectangle = Rectangle(7 , 5)
print(myRectangle.display())
print()
myParallelepipede = Parallelepipede(7 , 5 , 2)
print("the volume of myParallelepipede is: " , myParallelepipede.Volume())