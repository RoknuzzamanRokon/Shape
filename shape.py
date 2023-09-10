import math

class Shape:

    def area1(self):
        pass
    def perimeter1(self):
        pass

class Circle(Shape):

    def __init__(self, raduis):
        self.radius = raduis


    def area2(self):
        return math.pi * self.radius ** 2

    def perimeter2(self):
        return 2 * math.pi * self.radius




circle = Circle(5)
print(f"This is radius = {circle.radius}")
print(f"This is area = {circle.area2()}")
print(f"This is area with perimeter = {circle.perimeter2()}")



class Triangle(Shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height


    def area(self):
        calculate = (self.height * self.width) * .5
        return calculate


    def perimeter(self):
        return ((self.height * self.width) * .5) * 2


triangle = Triangle(3,4)
print(triangle.area())
print(triangle.perimeter())


