# Parse a JSON API response and turn part of it into a chart
import requests
import matplotlib.pyplot as plt
# API URL
url = "https://jsonplaceholder.typicode.com/posts"
# Send GET request
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    # Convert API response to JSON
    data = response.json()
    # Take first 10 posts
    posts = data[:10]
    # Extract post IDs
    post_ids = [post["id"] for post in posts]
    # Extract user IDs
    user_ids = [post["userId"] for post in posts]
    # Create bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(post_ids, user_ids)
    plt.title("User ID for First 10 Posts")
    plt.xlabel("Post ID")
    plt.ylabel("User ID")
    plt.show()
else:
    print("Failed to fetch data")
    print("Status code:", response.status_code)