#Step 1 : pull data from iTunes
import requests
import json
url = "https://itunes.apple.com/search?term=thor&media=movie"
response = requests.get(url)
print(f"Status is {response.status_code}")