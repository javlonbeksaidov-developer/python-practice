'''6-mashq — Bir nechta postlarni olish'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url)

data = response.json()

print(f"Status Code: {response.status_code}")
print(f"Jami postlar soni: {len(data)}")