from TASK5my_visualization import bar_chart, line_chart, pie_chart
# Sample dataset
products = ["Laptop", "Phone", "Tablet", "Watch", "Headphones"]
sales = [50, 80, 40, 30, 70]
# Use reusable functions
bar_chart(products, sales, "Product Sales")
line_chart(products, sales, "Product Sales Trend")
pie_chart(products, sales, "Product Sales Distribution")