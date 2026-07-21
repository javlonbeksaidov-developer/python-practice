'''9-mashq — userId bo'yicha filtrlash'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url=url)

data = response.json()


# for index in range(len(data)):
#     if data[index]['userId'] == 1:
#         print(f"Post ID: {data[index]['id']}.\nTitle: {data[index]['title']}")

for post in data:
    if post["userId"] == 1:
        print(post["title"])

