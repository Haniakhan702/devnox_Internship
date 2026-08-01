#NumPy practice program to create arrays, index/slice them, and compute basic statistics without loops
import numpy as np

# Take 5 numbers from the user
values = list(map(int, input("Enter 5 numbers separated by space: ").split()))

# Convert list to NumPy array
arr = np.array(values)

# Display array
print("Array:", arr)

# Indexing
print("Second element:", arr[1])

# Slicing
print("Middle three elements:", arr[1:4])

# Basic Statistics
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Largest:", np.max(arr))
print("Smallest:", np.min(arr))