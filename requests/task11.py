'''11-mashq — Xatolikni tekshirish'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts/999999'
response = requests.get(url=url)

data = response.json()

print(f"Status Code: {response.status_code}\nResponse: {data}")