'''6-mashq — find()'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

data = soup.find("h1")
print(data)