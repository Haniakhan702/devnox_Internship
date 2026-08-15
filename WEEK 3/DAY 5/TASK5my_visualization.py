# Build 2–3 reusable plotting functions (a tiny personal visualization module)
import matplotlib.pyplot as plt
# Bar chart function
def bar_chart(categories, values, title):
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.show()
# Line chart function
def line_chart(categories, values, title):
    plt.plot(categories, values, marker="o")
    plt.title(title)
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.show()
# Pie chart function
def pie_chart(categories, values, title):
    plt.pie(values, labels=categories, autopct="%1.1f%%")
    plt.title(title)
    plt.show()