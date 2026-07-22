# Program to check logical operators

age = int(input("Enter your age: "))

# and: both conditions must be true
if age >= 18 and age <= 60:
    print("You can work")

# or: at least one condition should be true
if age < 18 or age > 60:
    print("Not in working age group")

# not: reverses the condition
if not age < 18:
    print("You are not a child")



# Program to find sum of numbers using recursion
def sum_numbers(n):
    # Base condition: if n becomes 0, stop recursion
    if n == 0:
        return 0
    
    # Recursive call: add current number with smaller numbers
    return n + sum_numbers(n - 1)


# Taking input from user
num = int(input("Enter a number: "))

# Calling the function
total = sum_numbers(num)

# Printing result
print("Sum of numbers from 1 to", num, "is:", total)