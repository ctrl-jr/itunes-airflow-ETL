#Step 1 : pull data from iTunes
import requests
import json
url = "https://itunes.apple.com/search?term=thor&media=movie"
response = requests.get(url)

#Verifying that the connection is OK (expected code 200)
print(f"Status is {response.status_code}")

#Loading the downloaded text as a json string
json_obj = json.loads(response.text)
#We want to look into the _results_ key from the file 
results_array = json_obj["results"]
for result in results_array:
    runtime = (result["trackTimeMillis"] / 3600000) #Transforming the time from miliseconds to hours so we can get a proper runtime
    movie_name = result["trackName"] #The key _trackName_ contains the movie
    print(f"Movie:: {movie_name} - Runtime:: {round(runtime,1)}h")
