#!/usr/bin/python3
"""
Module task_02_requests
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        for fetched_data in response.json():
            print(fetched_data['title'])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder and save into a csv file
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        filename = "posts.csv"
        with open(filename, "w", encoding="utf-8") as csv_file:
            dict_list = ["id", "title", "body"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=dict_list)
            csv_writer.writeheader()
            for fetched_data in response.json():
                csv_writer.writerow({
                    "id": fetched_data['id'],
                    "title": fetched_data['title'],
                    "body": fetched_data['body']
                })
