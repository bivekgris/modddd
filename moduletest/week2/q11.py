class ComplexNumber:
    def __init__(self,real,img):
        self.re=real
        self.im=img
        
    def __add__(self,other):
        real=self.re+other.re
        img=self.im+other.im
        if img==0:
            return (f'{real} : real')
        
        if real==0:
            return (f'{img}i: Imaginary')
        
        if img<0:
            return (f'{real}{img}i')
        else:
            return (f'{real}+{img}i')
        
    def __str__(self):
        if self.im == 0:
            return '%.2f' % self.re
        if self.re == 0:
            return '%.2fi' % self.im
        if self.im < 0:
            return '%.2f - %.2fi' % (self.re, -self.im)
        else:
            return '%.2f + %.2fi' % (self.re, self.im)
  
def complexCalculator(real1 , imaginary1 , real2, imaginary2):
    c1 = ComplexNumber(real1,imaginary1)
    c2 = ComplexNumber(real2,imaginary2)
    return [ str(c1+c2) , str(c1-c2) , str(c1*c2) , str(c1/c2) ]
 
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(2, 4)
print(c1 + c2) 