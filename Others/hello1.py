import json
import requests
X = input("Write something here: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + X)
#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["country"])