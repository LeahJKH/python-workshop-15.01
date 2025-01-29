# i stedet for og bygge en fil for og  hente informasjon fra nettet bruker vi requests som er en ferdig bygd en
import requests
import json

Url = "https://miku-api.vercel.app/vocaloids/" # her putter vi inn url vi skal hente fra
Response = requests.get(Url)
JsonObj = Response.json() # vi gir koden beskjed at dette er en json fil

with open("vocaloids.json", "w") as file: #her gjør vi så vi lager en ny fil "w" står for write
    json.dump(JsonObj, file, indent=1) #her passer vi på at filen ser ut og ikke ser ut som knot