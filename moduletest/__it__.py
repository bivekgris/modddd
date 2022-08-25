class weight:
  def __init__(self, weight):
    self. weight= weight
  def __lt__(self,other):
    return self.weight<other.weight
a=weight(50)
b=weight(60)
c=weight(40)
print(c<a<b)