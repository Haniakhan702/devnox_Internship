# Take input from the user for the number of terms
num = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1

# Counter
count = 0

print("Fibonacci Series:")

# Print Fibonacci numbers using a while loop
while count < num:
    print(a, end=" ")

    # Calculate the next Fibonacci number
    c = a + b

    # Update the values
    a = b
    b = c

    # Increase the counter
    count += 1



# Function to find Fibonacci number using recursion
def fibonacci(n):

    # Base case
    if n <= 1:
        return n

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Take input from the user
terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

# Print Fibonacci numbers
for i in range(terms):
    print(fibonacci(i), end=" ")