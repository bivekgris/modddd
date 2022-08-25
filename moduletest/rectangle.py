class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    
    def Perimeter(self):
        return 2*(self.length+self.width)
    
    def Area(self):
        return self.length*self.width
    
    def display(self):
        return (f'Rectangle has length of {self.length} and width of {self.width} and has a perimeter and area as {Rectangle.Perimeter(self)}')
        
r=Rectangle(10,20)
print(r.display())
        
        
        