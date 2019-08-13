import json
import requests
import os

# res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
# body = json.loads(res.content)

# print(body.keys())
# print (body["name"])
# print(body["id"])
# print(body["types"])
# print(body["forms"])
# print(body["abilities"])
# print(body["height"])
# # print(body["moves"])
# print(body["sprites"])
# print(body["stats"])

key = os.environ.get("GIPHY_KEY")
url = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=pikachu&rating=g"
gifres = requests.get(url)
gifbody = json.loads(gifres.content)

print(gifbody.keys())
print(gifbody["data"][0]["url"])