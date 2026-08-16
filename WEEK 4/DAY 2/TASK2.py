# Simple linear regression from scratch using manual gradient descent
import numpy as np
# Training data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
# Start with simple values
m = 0
b = 0
# Learning rate
learning_rate = 0.01
# Number of iterations
epochs = 1000
# Number of data points
n = len(X)
# Gradient descent
for i in range(epochs):
    # Predictions
    y_pred = m * X + b
    # Calculate errors
    error = y_pred - y
    # Calculate gradients
    dm = (2 / n) * np.sum(X * error)
    db = (2 / n) * np.sum(error)
    # Update m and b
    m = m - learning_rate * dm
    b = b - learning_rate * db
# Final results
print("Slope (m):", m)
print("Intercept (b):", b)
# Predictions
predictions = m * X + b
print("\nPredictions:")
print(predictions)