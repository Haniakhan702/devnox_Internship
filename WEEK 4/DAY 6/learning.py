# Plot the decision boundary of a simple classifier on a 2D toy dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
# 2D dataset
X = np.array([
    [1, 1],
    [2, 2],
    [2, 1],
    [1, 2],
    [6, 6],
    [7, 7],
    [7, 6],
    [6, 7]
])
# Class labels
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
# Create the classifier
model = LogisticRegression()
# Train the classifier
model.fit(X, y)
# Create x values for the boundary
x_values = np.linspace(0, 8, 100)
# Get model coefficients
m = model.coef_[0]
b = model.intercept_[0]
# Calculate decision boundary
y_values = -(m[0] * x_values + b) / m[1]
# Plot Class 0
plt.scatter(
    X[y == 0, 0],
    X[y == 0, 1],
    label="Class 0"
)
# Plot Class 1
plt.scatter(
    X[y == 1, 0],
    X[y == 1, 1],
    label="Class 1"
)
# Plot decision boundary
plt.plot(
    x_values,
    y_values,
    label="Decision Boundary"
)
# Add labels and title
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Decision Boundary of Logistic Regression")
plt.legend()
#Show the graph
plt.show()