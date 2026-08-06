#Inheritance
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Circle(Shape):    # Child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self): # Override parent method
        return 3.14 * self.radius * self.radius

class Square(Shape): # Child inherits from Shape
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self): # Override parent method
        return self.side * self.side

class Triangle(Shape): # Child inherits from Shape
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self): # Override parent method
        return 0.5 * self.base * self.height

# Both Circle and Square inherit 'name' attribute from Shape
circle = Circle(5)
square = Square(4)
triangle = Triangle(6, 8)

print(circle.name)  # Output: Circle
print(square.name)  # Output: Square
print(triangle.name)  # Output: Triangle

print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16
print(triangle.area())  # Output: 24.0

# Polymorphism
def print_area(shape):
    print(f"The area of the {shape.name} is: {shape.area()}")

# Same method called on different behaviors
# print_area(circle)  # Output: The area of the Circle is: 78.5
# print_area(square)  # Output: The area of the Square is: 16
# print_area(triangle)  # Output: The area of the Triangle is: 24.0

# or with a list of shapes
shapes = [Circle(5), Square(4), Triangle(6, 8)]
for shape in shapes:
    print_area(shape)   # Same code, different results based on the object type