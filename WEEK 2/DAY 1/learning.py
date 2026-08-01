#JSON File to Store and Display Book Records 
import json

# Book data
books = [
    {"Title": "Python", "Price": 1000},
    {"Title": "Java", "Price": 1200},
    {"Title": "C++", "Price": 900}
]

# Write data to JSON file
with open("books.json", "w") as file:
    json.dump(books, file)

# Read data from JSON file
with open("books.json", "r") as file:
    data = json.load(file)

# Display records
print("Book Records:")

for book in data:
    print("Title:", book["Title"], "Price:", book["Price"])



#CSV File to Store and Display Employee Records
import csv

# Write data to CSV file
with open("employee.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Salary"])

    # Employee records
    writer.writerow(["Ali", 50000])
    writer.writerow(["Sara", 45000])
    writer.writerow(["Ahmed", 60000])

# Read the CSV file
print("Employee Records:")

with open("employee.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)   # Skip header

    for row in reader:
        print("Name:", row[0], "Salary:", row[1])