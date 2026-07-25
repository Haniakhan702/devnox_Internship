# Student Record App

# List to store student names
students = []

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added.")

# Function to view students
def view_students():
    print("Student List:")
    for name in students:
        print("-", name)

# Main Program
while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")




# Keep asking until the user enters a valid float

while True:

    try:
        num = float(input("Enter a decimal number: "))
        print("You entered:", num)
        break

    except ValueError:
        print("Invalid input! Please enter a decimal number.")