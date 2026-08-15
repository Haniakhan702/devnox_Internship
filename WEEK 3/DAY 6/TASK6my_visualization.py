import matplotlib.pyplot as plt
# Sample data
subjects = ["Math", "English", "Physics", "Computer"]
marks = [85, 72, 90, 95]
# Bar chart
plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()