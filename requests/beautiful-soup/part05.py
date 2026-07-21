'''5-mashq — HTML ni chiroyli chiqarish'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())      # html kodini chiroyli konsolga chiqaradi 