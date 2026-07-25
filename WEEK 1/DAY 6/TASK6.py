# Exception-Safe Code (Keep Asking Until a Valid Integer is Entered)

# Keep asking until the user enters a valid integer

while True:

    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break

    except ValueError:
        print("Invalid input! Please enter an integer.")



 #Simple To-Do List App (Add / Remove / View Tasks)

 #  List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

# Function to remove a task
def remove_task():
    task = input("Enter task to remove: ")

    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

# Function to view tasks
def view_tasks():
    print("Your Tasks:")
    for task in tasks:
        print("-", task)

# Main Program
while True:

    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        remove_task()

    elif choice == 3:
        view_tasks()

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")