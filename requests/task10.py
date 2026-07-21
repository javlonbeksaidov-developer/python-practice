'''10-mashq — Params ishlatish'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts'


params = {
    'userId' : 1,
    'id' : 4,
}

response = requests.get(url=url, params=params)

data = response.json()

print(f"Status code: {response.status_code}")
print(f"URL: {response.url}")
