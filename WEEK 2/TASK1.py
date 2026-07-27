# Read , Write and Filter record in CSV file
import csv
with open("students.csv", "w" , newline='')as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
  # Student records
    writer.writerow(["Ali", 85])
    writer.writerow(["Sara", 70])
    writer.writerow(["Ahmed", 92])
print("student records written to students.csv")
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)   # Skip header

    for row in reader:
        if int(row[1]) > 80:
            print(row[0], row[1])


# Read , Write and Filter record in Json file
import json

# Student data
students = [
    {"Name": "Ali", "Marks": 85},
    {"Name": "Sara", "Marks": 70},
    {"Name": "Ahmed", "Marks": 92}
]

# Write data to JSON file
with open("students.json", "w") as file:
    json.dump(students, file)

# Read data from JSON file
with open("students.json", "r") as file:
    data = json.load(file)

# Filter records
print("Students with marks greater than 80:")

for student in data:
    if student["Marks"] < 80:
        print(student["Name"], student["Marks"])  