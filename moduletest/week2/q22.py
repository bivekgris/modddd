from re import S


class Shape():
    def area(self,geometry,*args):
        if geometry=='Square':
            return (args[0]*args[1])
        elif geometry == "Rectangle":
            return (args[0]*args[1])
        elif geometry == "Triangle":
            return (0.5*args[0]*args[1])
        elif geometry == "Trapezoid":
            return (((args[0]+args[1])*args[2])/2)

def checkshape():
    s=Shape()
    return s

print(checkshape().area('Trapezoid',2,4,5))
        