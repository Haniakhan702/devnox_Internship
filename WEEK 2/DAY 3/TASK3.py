# Pandas practice program that load a dataset,filter rows,group by a column,and handle missing values.
import pandas as pd

# Load the dataset
data = pd.read_csv("WEEK 2/DAY 3/students.csv")

# Display original data
print("Original Data:")
print(data)

# Handle missing values
# Fill missing marks with 0
data["Marks"] = data["Marks"].fillna(0)

print("\nData After Handling Missing Values:")
print(data)

# Filter rows (Marks greater than or equal to 80)
filtered_data = data[data["Marks"] >= 80]

print("\nStudents with Marks >= 80:")
print(filtered_data)

# Group by Department and find average marks
grouped_data = data.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(grouped_data)