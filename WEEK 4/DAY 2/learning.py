# Simple linear regression from scratch using manual gradient descent
import numpy as np
# Training data
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])
# Initial values
m = 0
b = 0
# Settings
learning_rate = 0.01
epochs = 1000
n = len(X)
# Gradient Descent
for i in range(epochs):
    # Make predictions
    y_pred = m * X + b
    # Calculate error
    error = y_pred - y
    # Calculate gradients
    dm = (2 / n) * np.sum(X * error)
    db = (2 / n) * np.sum(error)
    # Update slope and intercept
    m = m - learning_rate * dm
    b = b - learning_rate * db
# Display results
print("Slope:", m)
print("Intercept:", b)
# Final predictions
predictions = m * X + b
print("Predictions:", predictions)