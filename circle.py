import math
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    def area(self):
        area = math.pi * (self.r**2)
        return area
    def perimeter(self):
        perimeter = 2 * math.pi * self.r
        return perimeter


