# Marks Predictor & Pass/Fail Classifier — one regression model predicting marks from study hours,
# and one classifier predicting pass/fail
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score
# Dataset
study_hours = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
marks = np.array([35, 42, 50, 55, 65, 72, 80, 88])
# Pass = 1, Fail = 0
pass_fail = np.array([0, 0, 0, 1, 1, 1, 1, 1])

# Marks Prediction - Regression
regression_model = LinearRegression()
regression_model.fit(study_hours, marks)
predicted_marks = regression_model.predict(study_hours)
mae = mean_absolute_error(marks, predicted_marks)
r2 = r2_score(marks, predicted_marks)

# Pass/Fail - Classification
classification_model = LogisticRegression()
classification_model.fit(study_hours, pass_fail)
predicted_pass_fail = classification_model.predict(study_hours)
accuracy = accuracy_score(pass_fail, predicted_pass_fail)

# Test a new student
new_student = np.array([[6]])
predicted_mark = regression_model.predict(new_student)
predicted_result = classification_model.predict(new_student)
# Display results
print("MARKS PREDICTOR")
print("----------------")
print("Study Hours:", study_hours.flatten())
print("Actual Marks:", marks)
print("\nPredicted Marks:")
print(np.round(predicted_marks, 2))
print("\nRegression Evaluation:")
print("MAE:", round(mae, 2))
print("R² Score:", round(r2, 2))
print("\nPASS/FAIL CLASSIFIER")
print("---------------------")
print("Actual Results:", pass_fail)
print("Predicted Results:", predicted_pass_fail)
print("\nClassification Evaluation:")
print("Accuracy:", round(accuracy, 2))
print("\nNEW STUDENT")
print("------------")
print("Study Hours:", new_student[0][0])
print("Predicted Marks:", round(predicted_mark[0], 2))
if predicted_result[0] == 1:
    print("Predicted Result: PASS")
else:
    print("Predicted Result: FAIL")
    
# Short Evaluation Summary
print("\nEVALUATION SUMMARY")
print("-------------------")
print(
    "The regression model predicts marks from study hours. "
    "MAE shows the average prediction error, while R² shows "
    "how well study hours explain the marks."
)
print(
    "The classification model predicts whether a student will "
    "pass or fail. Accuracy shows the percentage of correct "
    "Pass/Fail predictions."
)