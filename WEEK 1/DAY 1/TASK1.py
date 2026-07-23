# Initialize the values
a = 20
b = 10

# Swap the values
a, b = b, a
print("a =", a)
print("b =", b)



# Function to reverse a string
def reverse_string(text):
    reverse = ""

    for i in text:
        reverse = i + reverse

    return reverse

# Take input from the user
text = input("Enter a string: ")

# Display the reversed string
print("Reversed String:", reverse_string(text))