'''7-mashq — find_all()'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

data = soup.find_all("p")
print(len(data))
for i in data:
    print(i.text)