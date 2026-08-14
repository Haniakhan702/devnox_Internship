# a correlation heatmap for a numeric dataset using Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample numeric dataset
data = {
    "Math": [80, 85, 90, 75, 95],
    "Physics": [78, 82, 88, 70, 92],
    "Computer": [90, 95, 92, 85, 98],
    "English": [70, 75, 80, 65, 85]
}
# Create DataFrame
df = pd.DataFrame(data)
# Calculate correlation
correlation = df.corr()
# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()