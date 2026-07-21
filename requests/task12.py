'''12-mashq — POST so'rovi'''

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python Requests",
    "body": "Learning API",
    "userId": 1
}

response = requests.post(url=url, json=data)

print("Status Code:", response.status_code)
print(f"Response: {response}")
print(response.json())