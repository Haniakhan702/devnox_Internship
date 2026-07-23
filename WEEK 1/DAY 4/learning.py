# Function to find the sum
def total(numbers):
    return sum(numbers)

# Take input from the user
numbers = list(map(int, input("Enter numbers: ").split()))

# Display result
print("Sum =", total(numbers))


# Function to count vowels
def count_vowels(text):
    count = 0

    for letter in text:
        if letter in "aeiouAEIOU":
            count += 1

    return count

# Take input from the user
text = input("Enter a string: ")

# Display result
print("Number of vowels:", count_vowels(text))



# Create Car class
class Car:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display details
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Take input from the user
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create object
car = Car(brand, model)

# Display details
car.display()