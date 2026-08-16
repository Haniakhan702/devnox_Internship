# Compute mean, median, standard deviation, and variance
import numpy as np
data = np.array([3, 5, 7, 7, 8, 10, 12])
# NumPy calculations
mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
std = np.std(data)
# Display results
print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std)