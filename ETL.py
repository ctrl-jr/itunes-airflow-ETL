#Step 1 : pull data from iTunes
import requests
import json
import pandas as pd
url = "https://itunes.apple.com/search?term=avengers&media=movie"
response = requests.get(url)

#Verifying that the connection is OK (expected code 200)
print(f"Status is {response.status_code} !")

#Loading the downloaded text as a json string
json_obj = json.loads(response.text)
#We want to look into the _results_ key from the file 
results_array = json_obj["results"]
movie_list = []
for result in results_array:
    if result["primaryGenreName"] == "Action & Adventure":
        refined_result = {
                        "movie" : result["trackName"], #The key _trackName_ contains the movie,
                        "runtime": round((result["trackTimeMillis"] / 3600000),2), #Transforming the time from miliseconds to hours so we can get a proper runtime
                        "genre" : result["primaryGenreName"] }

    movie_list.append(refined_result)
    else: pass

    #print(f"Movie:: {movie_name}") #- Runtime:: {round(runtime,1)}h")
print(movie_list)
#Creating a dataframe of our move list
df = pd.DataFrame(movie_list)
#Creating a local CSV to view the list
df.to_csv("avengers_movies.csv")