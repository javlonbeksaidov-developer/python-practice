from bs4 import BeautifulSoup
import requests
import json

url = "https://www.fcbarcelona.com/en/football/first-team/players"
response = requests.get(url=url)

FILENAME = "barselona.json"

soup = BeautifulSoup(response.text, "html.parser")

try:
    with open(FILENAME, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []


block = soup.find_all("figcaption")

for player in block:
    number = player.find("span", attrs={"class": "team-person__number"})

    fname = player.find("span", attrs={"class": "team-person__first-name"})

    lname = player.find("span", attrs={"class": "team-person__last-name"})

    position = player.find("li", attrs={"class": "team-person__position-meta"})

    players = {
        "number": number.text.strip() if number else "",
        "fname": fname.text.strip() if fname else "",
        "lname": lname.text.strip() if lname else "",
        "position": position.text.strip() if lname else "",
    }
    data.append(players)


with open(FILENAME, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
