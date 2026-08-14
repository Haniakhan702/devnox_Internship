# fetch data from a public REST API and save it as a JSON file
import requests
import json
# API URL
url = "https://jsonplaceholder.typicode.com/posts"
# Send GET request
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    data = response.json()
    # Save data to a JSON file
    with open("posts.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data fetched successfully!")
    print("Data saved to posts.json")

else:
    print("Failed to fetch data")
    print("Status code:", response.status_code)