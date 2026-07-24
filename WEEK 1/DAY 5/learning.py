 # Find Square of a Number
try:
   
    # Take input from the user
    num = int(input("Enter a number: "))

    # Find square
    print("Square =", num * num)

# Handle invalid input
except ValueError:
    print("Error! Please enter a valid number.")



# Inheritance (Vehicle → Car and Bike)
    # Parent class
class Vehicle:

    # Method
    def start(self):
        print("Vehicle is starting")

# Child class
class Car(Vehicle):

    def start(self):
        print("Car is starting")

# Child class
class Bike(Vehicle):

    def start(self):
        print("Bike is starting")

# Create objects
car = Car()
bike = Bike()

# Call methods
car.start()
bike.start()