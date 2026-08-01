#NumPy practice program to create arrays, index/slice them, and compute basic statistics without loops
import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50, 60])

# Print the array
print("Array:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[3:])

# Basic Statistics
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Standard Deviation:", np.std(numbers))



