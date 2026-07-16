import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print()
print("Number of astronauts:", data["number"])
print()

for astronaut in data["people"]:
    print(astronaut["name"], "-", astronaut["craft"])