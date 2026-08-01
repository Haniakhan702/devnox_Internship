# Merge two small datasets (dictionaries or DataFrames) and produce a summary.
import pandas as pd
# First dataset
students = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Ahmed"]
}
# Second dataset
marks = {
    "ID": [1, 2, 3],
    "Marks": [85, 90, 78]
}
# Convert dictionaries into DataFrames
df_students = pd.DataFrame(students)
df_marks = pd.DataFrame(marks)
# Merge both DataFrames using the ID column
result = pd.merge(df_students, df_marks, on="ID")
# Display merged data
print("Merged Data:")
print(result)
# Summary
print("\nSummary:")
print("Total Students:", len(result))
print("Average Marks:", result["Marks"].mean())
print("Highest Marks:", result["Marks"].max())
print("Lowest Marks:", result["Marks"].min())