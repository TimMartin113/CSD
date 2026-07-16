import requests

response = requests.get("http://www.google.com")

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Connection successful!")
else:
    print("Connection failed.")