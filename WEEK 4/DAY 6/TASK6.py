# Plot the decision boundary of a simple classifier on a 2D toy dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
# simple 2D dataset
X = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [2, 2],
    [6, 6],
    [7, 6],
    [6, 7],
    [7, 7]
])
# 0 = Class 0, 1 = Class 1
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
# Create and train the classifier
model = LogisticRegression()
model.fit(X, y)
# Create points for the decision boundary
x_values = np.linspace(0, 8, 100)
# Get model parameters
m = model.coef_[0]
b = model.intercept_[0]
# Decision boundary:
# m[0]*x + m[1]*y + b = 0
y_values = -(m[0] * x_values + b) / m[1]
# Plot the data
plt.scatter(X[y == 0, 0], X[y == 0, 1], label="Class 0")
plt.scatter(X[y == 1, 0], X[y == 1, 1], label="Class 1")
# Plot decision boundary
plt.plot(x_values, y_values, label="Decision Boundary")
# Add labels
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Decision Boundary")
plt.legend()
# Show graph
plt.show()