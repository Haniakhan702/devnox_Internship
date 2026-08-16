# Train scikit-learn's LinearRegression on a small dataset and evaluate with MAE, MSE, and R²
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# 1. Create a small dataset
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 5, 7, 8, 11, 12])
# 2. Create the model
model = LinearRegression()
# 3. Train the model
model.fit(X, y)
# 4. Make predictions
y_pred = model.predict(X)
# 5. Calculate evaluation metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
# 6. Display results
print("Actual values:")
print(y)
print("\nPredicted values:")
print(y_pred)
print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("R²:", r2)
# 7. Display the learned equation
print("\nModel:")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)