# Import math module for the value of pi
import math


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Function to calculate the area of a circle
def area_circle(radius):
    return math.pi * radius * radius


# Function to calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width


# -------- Main Program --------

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Area of Circle")
print("4. Area of Rectangle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(f))

elif choice == 3:
    radius = float(input("Enter the radius: "))
    print("Area of Circle:", area_circle(radius))

elif choice == 4:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print("Area of Rectangle:", area_rectangle(length, width))

else:
    print("Invalid Choice!")




# Create Student class
class Student:

    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to calculate grade
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

# Take input from the user
name = input("Enter Student Name: ")
marks = int(input("Enter Student Marks: "))

# Create object
student = Student(name, marks)

# Display result
print("Name:", student.name)
print("Marks:", student.marks)
print("Grade:", student.grade())