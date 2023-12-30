class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = (self.width*2) + (self.length*2)
        return perimeter

    def area(self):
        area = self.width * self.length
        return area

    def get_details(self):
        return f"The length is {self.length}, the width is {self.width}, the perimeter is {self.perimeter()}cm and the area is {self.area()}cm2"

class Parallelepiped(Rectangle):

    def __init__(self,length, width, height):
        super().__init__(length,width)

        self.height = height

    def volume(self):
        volume = self.area() * self.height
        return volume
    def get_details(self):
        return f"The length of the parallelepiped is {self.length}, the width is {self.width}, the height is {self.height}, the perimeter is {self.perimeter()}cm, the area is {self.area()}cm2 and the volume is {self.volume()}"

x = Rectangle(7,5)
print(x.get_details())

y = Parallelepiped(7,5,2)
print(y.get_details())


