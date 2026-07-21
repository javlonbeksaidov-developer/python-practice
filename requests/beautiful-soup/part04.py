'''4-mashq — Linkni topish'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

data =soup.find("a")
print(data)
print(f"MATN: {data.text}")
print(f"LINK: {data['href']}")