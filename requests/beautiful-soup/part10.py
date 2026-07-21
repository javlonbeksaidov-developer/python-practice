'''10-mashq — Mini loyiha'''

from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response =requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

def show(tag):
    print("=" * 15)
    print(f"Tag name: {tag.name.title()}")
    print(f"{tag.text}")

    if tag.has_attr("href"):
        print(f"Link: {tag['href']}")

title = soup.find('title')
heading = soup.find("h1")
paragraph = soup.find("p")
link = soup.find("a")

show(title)
show(heading)
show(paragraph)
show(link)

print("=" * 15)