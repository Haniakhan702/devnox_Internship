# Student Grade Calculator
 
# Function to calculate grade
def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


# Main Program
try:

    # Take input from the user
    marks = int(input("Enter your marks: "))

    # Check if marks are valid
    if marks < 0 or marks > 100:
        print("Please enter marks between 0 and 100.")

    else:
        # Display the grade
        print("Your Grade is:", calculate_grade(marks))

# Handle invalid input
except ValueError:
    print("Invalid input! Please enter numbers only.")



