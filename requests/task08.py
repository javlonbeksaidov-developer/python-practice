'''8-mashq — Birinchi 10 ta sarlavha'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url=url)

data = response.json()

for index in range(10):
    print(f"{index+1}. {data[index]['title']}")
