# Take a messy CSV (duplicates, missing values, inconsistent formats) and output a cleaned CSV
import pandas as pd

# Read CSV file
data = pd.read_csv("WEEK 2/WEEK 2 Mini Project/students.csv")

# Count original rows
original_rows = len(data)

# Remove duplicate rows
data = data.drop_duplicates()
duplicates_removed = original_rows - len(data)

# Count missing values
missing_values = data["Age"].isnull().sum()

# Fill missing Age with 0
data["Age"] = data["Age"].fillna(0)

# Make city names consistent
data["City"] = data["City"].str.title()

# Save cleaned data
data.to_csv("cleaned_students.csv", index=False)

# Print summary report
print("----- Data Cleaning Summary -----")
print("Duplicate rows removed:", duplicates_removed)
print("Missing values filled:", missing_values)
print("City names standardized.")
print("Cleaned file saved as cleaned_students.csv")