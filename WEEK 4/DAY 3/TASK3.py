# Train scikit-learn's LinearRegression on a small dataset and evaluate with MAE, MSE, and R²
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Small dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])
# Create the model
model = LinearRegression()
# Train the model
model.fit(X, y)
# Make predictions
y_pred = model.predict(X)
# Evaluate the model
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
# Display results
print("Actual values:", y)
print("Predicted values:", y_pred)
print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("R²:", r2)
print("\nModel Parameters:")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)