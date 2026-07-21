'''4-mashq — Type tekshirish'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url=url)

print(type(response))
print(type(response.text))
print(type(response.json()))