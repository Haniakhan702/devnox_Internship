# Plot a bar chart, a line chart, and a pie chart from a sample dataset
import matplotlib.pyplot as plt

# Sample dataset
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 140, 200, 170]

# BAR CHART 
plt.figure(figsize=(7, 5))
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# LINE CHART
plt.figure(figsize=(7, 5))
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# PIE CHART 
plt.figure(figsize=(7, 5))
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Monthly Sales - Pie Chart")
plt.show()