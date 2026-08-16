# Compute mean, median, standard deviation, and variance
import numpy as np
# Dataset
data = np.array([2, 4, 4, 6, 8])
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