from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display(self):
        print('This is a shape.')

class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle (Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area (self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
circle = Circle(5)
rectangle = Rectangle(4,6)

circle.display()
print(f'Circle Area: {circle.area()}')
print(f'Circle Perimeter {circle.perimeter()}')

rectangle.display()
print(f'Rectangle Area: {rectangle.area()}')
print(f'Rectangle Perimeter {rectangle.perimeter()}')











