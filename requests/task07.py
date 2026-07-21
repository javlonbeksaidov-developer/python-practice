"""7-mashq — Birinchi post"""

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url=url)

data = response.json()

print(f"ID: {data[0]['id']}\nTitle: {data[0]['title']}\nBody: {data[0]['body']}")
