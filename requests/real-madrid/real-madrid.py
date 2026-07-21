from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.realmadrid.com/en-US/football/first-team/players'
response = requests.get(url=url)

FILENAME = 'realmadrid.json'

soup = BeautifulSoup(response.text, 'html.parser')

try:
    with open(FILENAME, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []


block = soup.find_all("app-player-profile-card")

for player in block:
    number = player.find("h4", attrs={"class":"profile-card__number"})
    name = player.find("h4", attrs={"class":"profile-card__name"})
    position = player.find("p", attrs={"class":"profile-card__role"})

    players = {
        "number" : number.text.strip() if number else "",
        "name" : name.text.strip() if name else "",
        "position" : position.text.strip() if position else "",
    }
    data.append(players)


with open(FILENAME, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)