# Fetch users and save to JSON
import requests
import json
# API URL
url = "https://jsonplaceholder.typicode.com/users"
# Send GET request
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    # Save data to file
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Users saved successfully!")

else:
    print("Failed to fetch users")
    print("Status code:", response.status_code)