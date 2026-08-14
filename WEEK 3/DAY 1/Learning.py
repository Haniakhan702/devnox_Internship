# Create a Python program that plots the marks of 5 students.
import matplotlib.pyplot as plt
# Sample dataset
students = ["Ali", "Sara", "Ahmed", "Hina", "Usman"]
marks = [78, 92, 65, 88, 74]
# BAR CHART 
plt.figure(figsize=(9, 6))
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Sample dataset for line chart
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [32, 34, 33, 35, 31, 30, 29]
# LINE CHART
plt.figure(figsize=(7, 5))
plt.plot(days, temperature, marker="o")
plt.title("Weekly Temperature - Line Chart")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

# Sample dataset for pie chart
languages = ["Python", "Java", "C++", "JavaScript"]
students = [45, 25, 15, 35]
# PIE CHART 
plt.figure(figsize=(7, 5))
plt.pie(students, labels=languages, autopct="%1.1f%%")
plt.title("Student Distribution by Programming Language")
plt.show()