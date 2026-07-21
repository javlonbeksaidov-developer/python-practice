'''8-mashq — Tag nomini chiqarish'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find("title")

print(f"Tag: {title.name}")         # teg nomini chiqaradi.
print(f"Text: {title.text}")        # tegdagi textni chiqaradi.