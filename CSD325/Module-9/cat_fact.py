import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

# Test the connection
print("Status Code:", response.status_code)
print()

# Print the raw response
print("Raw Response:")
print(response.text)

print()

# Print formatted response
if response.status_code == 200:
    data = response.json()

    print("Formatted Output")
    print("----------------")
    print("Cat Fact:")
    print(data["fact"])
    print()
    print("Length:", data["length"], "characters")