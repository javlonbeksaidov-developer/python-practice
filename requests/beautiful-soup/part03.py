'''3-mashq — Birinchi <p>'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

data = soup.find("p")
print(data)