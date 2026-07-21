'''5-mashq — Headers'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.headers["Content-Type"])
print(response.headers["Date"])

for key, value in response.headers.items():
    print(key, ":", value)