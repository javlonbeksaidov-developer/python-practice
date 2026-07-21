'''2-mashq — Matnni chiqarish'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url=url)

data = response.text
print(data)