import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Sample dataset
data = {
    "Math": [80, 85, 90, 70, 95, 88],
    "Physics": [75, 82, 89, 68, 92, 85],
    "Computer": [90, 95, 94, 80, 98, 91],
    "English": [65, 70, 78, 60, 85, 75],
    "Chemistry": [72, 80, 88, 65, 90, 82]
}
# Create DataFrame
df = pd.DataFrame(data)
# Calculate correlation
correlation = df.corr()
# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Student Subject Correlation")
plt.show()