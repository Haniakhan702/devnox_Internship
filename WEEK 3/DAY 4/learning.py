# Fetch Todo Data and Save It
import requests
import json
# API URL
url = "https://jsonplaceholder.typicode.com/todos"
# Send GET request
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    # Save data to a JSON file
    with open("todos.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Todo data fetched successfully!")
    print("Data saved to todos.json")

else:
    print("Failed to fetch data")
    print("Status code:", response.status_code)