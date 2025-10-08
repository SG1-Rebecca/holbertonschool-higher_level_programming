import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post_data in posts:
            print(post_data['title'])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        filename = "posts.csv"
        with open(filename, "w", encoding="utf-8") as csv_file:
            csv_write = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            csv_write.writeheader()
            for post_data in posts:
                csv_write.writerow({'id': post_data['id'], 'title': post_data['title'], 'body': post_data['body']})
    else:
        print("Failed to fetch posts")
