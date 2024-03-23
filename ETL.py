#Step 1 : pull data from iTunes
import requests
import json
import pandas as pd
import datetime as dt

def run_itunes_etl():
    url = "https://itunes.apple.com/search?term=avengers&media=movie"
    response = requests.get(url)

    #Verifying that the connection is OK (expected code 200)
    print(f"Status is {response.status_code} !")

    #Loading the downloaded text as a json string
    json_obj = json.loads(response.text)
    #We want to look into the _results_ key from the file 
    results_array = json_obj["results"]
    #initializing an empty list 
    movie_list = []
    for result in results_array:
        if result["primaryGenreName"] != "Action & Adventure":
            continue
        else:
            refined_result = {
                            "movie" : result["trackName"], #The key _trackName_ contains the movie title
                            "temp_year": result["releaseDate"],
                            "runtime": round((result["trackTimeMillis"] / 3600000),1), #Transforming the time from miliseconds to hours so we can get a proper runtime
                            "genre" : result["primaryGenreName"],
                            "director" : result["artistName"] }

        movie_list.append(refined_result)
        
    #print(movie_list)
    #Creating a dataframe of our move list
    df = pd.DataFrame(movie_list)
    #Extracting year from yyyy-mm-dd-hh-mmTZ
    df['year'] = pd.DatetimeIndex(df['temp_year']).year
    #Making a new df excluding old year format
    new_df = df[['movie', 'year', 'runtime', 'director' ]]
    new_df = new_df.sort_values(by=['year'])
    print(new_df)
    #Creating a local CSV to view the list
    new_df.to_csv("avengers_movies.csv")

    #added random comment
