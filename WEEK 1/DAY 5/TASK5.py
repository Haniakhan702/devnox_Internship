#Create 3 Classes Demonstrating Inheritance (Shape → Circle/Rectangle)
#  Parent class
class Shape:

    # Area method
    def area(self):
        print("Area of Shape")

# Child class Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle =", 3.14 * self.radius * self.radius)

# Child class Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle =", self.length * self.width)

# Create objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call area method
circle.area()
rectangle.area()



# Handle Division by Zero and Invalid Input Using try/except
try:
    # Take input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Divide the numbers
    result = num1 / num2

    print("Result =", result)

# Handle division by zero
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

# Handle invalid input
except ValueError:
    print("Error! Please enter numbers only.")