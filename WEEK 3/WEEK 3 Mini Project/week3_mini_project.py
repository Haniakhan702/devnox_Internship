# EDA Mini-Dashboard Script — load a public dataset (or fetched API data), auto-generate 4 charts, and write 3–4 sentences of insight based on what the charts show
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Fetch data from public API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    # Convert API response to JSON
    data = response.json()
    # Create DataFrame
    df = pd.DataFrame(data)
    print("Data loaded successfully!")
    print(df.head())
    # CHART 1
    # Number of posts by user
    user_posts = df["userId"].value_counts()
    plt.figure(figsize=(8, 5))
    user_posts.plot(kind="bar")
    plt.title("Number of Posts by User")
    plt.xlabel("User ID")
    plt.ylabel("Number of Posts")
    plt.show()
    # CHART 2
    # Post ID trend
    plt.figure(figsize=(8, 5))
    plt.plot(df["id"], df["userId"], marker="o")
    plt.title("User ID Across Posts")
    plt.xlabel("Post ID")
    plt.ylabel("User ID")
    plt.show()
    # CHART 3 
    # Distribution of posts by user
    plt.figure(figsize=(7, 5))
    user_posts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Post Distribution by User")
    plt.ylabel("")
    plt.show()
    # CHART 4
    # Correlation heatmap
    plt.figure(figsize=(7, 5))
    sns.heatmap(
        df[["userId", "id"]].corr(),
        annot=True,
        cmap="coolwarm"
    )
    plt.title("Correlation Heatmap")
    plt.show()
    #INSIGHTS 
    print("\nINSIGHTS:")
    print("1. Each user contributes a different number of posts.")
    print("2. The post IDs increase continuously as more posts are listed.")
    print("3. The pie chart shows how posts are distributed among users.")
    print("4. The heatmap shows the correlation between post ID and user ID.")
else:
    print("Failed to fetch data")
    print("Status code:", response.status_code)