import requests
import json

Url = "https://miku-api.vercel.app/vocaloids/"
Response = requests.get(Url)
JsonObj = Response.json()

with open("vocaloids.json", "w") as file:
    json.dump(JsonObj, file, indent=1)