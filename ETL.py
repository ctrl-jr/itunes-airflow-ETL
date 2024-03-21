#Step 1 : pull data from iTunes
import requests
import json
url = "https://itunes.apple.com/search?term=thor&media=movie"
response = requests.get(url)
print(type(response))
#Verifying that the connection is OK (expected code 200)
# print(f"Status is {response.status_code}")

# #Loading
# json_obj = json.loads(response.text)
# results_array = json_obj["results"]
# for result in results_array:
#     runtime = (result["trackTimeMillis"] / 3600000)
#     movie_name = result["trackName"]
#     print(f"Movie:: {movie_name} - Runtime:: {round(runtime,1)}h")
