# Merge two small datasets (dictionaries or DataFrames) and produce a summary.
import pandas as pd

# Employee names
employees = {
    "ID": [101, 102, 103],
    "Name": ["Ayesha", "Bilal", "Fatima"]
}

# Employee salaries
salary = {
    "ID": [101, 102, 103],
    "Salary": [50000, 60000, 55000]
}

# Create DataFrames
df1 = pd.DataFrame(employees)
df2 = pd.DataFrame(salary)

# Merge DataFrames
merged = pd.merge(df1, df2, on="ID")

# Display merged data
print("Merged Data:")
print(merged)

# Summary
print("\nSummary:")
print("Total Employees:", len(merged))
print("Average Salary:", merged["Salary"].mean())
print("Highest Salary:", merged["Salary"].max())
print("Lowest Salary:", merged["Salary"].min())