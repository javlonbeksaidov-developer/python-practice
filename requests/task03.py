'''3-mashq — JSON'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url=url)

data = response.json()

print(f"ID: {data['id']}\nTitle: {data['title']}\nBody: {data['body']}")