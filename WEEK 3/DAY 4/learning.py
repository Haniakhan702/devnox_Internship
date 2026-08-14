# Parse a JSON API response and turn part of it into a chart
import requests
import matplotlib.pyplot as plt
# API URL
url = "https://jsonplaceholder.typicode.com/posts"
# Get data from API
response = requests.get(url)
# Check if request was successful
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    # Take first 5 posts
    posts = data[:5]
    # Get post IDs
    post_ids = [post["id"] for post in posts]
    # Get user IDs
    user_ids = [post["userId"] for post in posts]
    # Create bar chart
    plt.bar(post_ids, user_ids)
    plt.title("User IDs of First 5 Posts")
    plt.xlabel("Post ID")
    plt.ylabel("User ID")
    plt.show()
else:
    print("Something went wrong")