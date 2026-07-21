from bs4 import BeautifulSoup
import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://ufa.uz/naczionalnaya-sbornaya-uzbekistana/"
response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

FILENAME = 'uzbekistan.json'
try:
    with open(FILENAME, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []


players = soup.find_all(class_="vc_column_container")

for player in players:
    name = player.find("h2", attrs={"class":"wpb_heading"})

    azo = {
        "name" : name.text.strip() if name else "",
    }
    data.append(azo)



with open(FILENAME, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)