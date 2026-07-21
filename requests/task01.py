'''1-mashq — Birinchi GET so'rovi'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url=url)

print(f"Status code: {response.status_code}")
print(f"URL: {response.url}")
