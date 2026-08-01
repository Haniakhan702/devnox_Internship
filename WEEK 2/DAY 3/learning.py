# Pandas practice program that load a dataset,filter rows,group by a column,and handle missing values.
import pandas as pd

# Load dataset
employees = pd.read_csv("WEEK 2/DAY 3/employees.csv")

# Display data
print("Original Data:")
print(employees)

# Replace missing salaries with 0
employees["Salary"] = employees["Salary"].fillna(0)

# Filter employees with salary greater than 50000
high_salary = employees[employees["Salary"] > 50000]

print("\nEmployees with Salary > 50000:")
print(high_salary)

# Group by department and calculate average salary
average_salary = employees.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(average_salary)