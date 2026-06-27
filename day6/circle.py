import math
class Circle:
    def __init__(self,r):
        self.rad=r
    def area(self):
          return math.pi**(self.rad)
    def perimeter(self):
        return 2*math.pi*self.rad
c1= Circle(20)
print(c1.area())