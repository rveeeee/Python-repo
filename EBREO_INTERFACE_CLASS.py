from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod

    def draw (self):
        pass

class Circle (Drawable):
    def draw(self):
        return "Drawing a circle"
    
class Rectangle (Drawable):
    def draw(self):
        return "Drawing a rectangle"

circle = Circle()
rectangle = Rectangle()

print(circle.draw())
print(rectangle.draw())