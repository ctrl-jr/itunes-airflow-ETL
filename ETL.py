#Step 1 : pull data from iTunes
import requests
import json
import pandas as pd
import datetime as dt
from pprint import pprint 
# import boto3
# import os
# import pathlib
# import fastparquet

#def run_itunes_etl():
url = "https://itunes.apple.com/search?term=avengers&media=movie"
response = requests.get(url)

#Verifying that the connection is OK (expected code 200)
#print(f"Status is {response.status_code} !")
pprint(response) 

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
#new_df = new_df.reset_index(drop=True) #removing index

#print(new_df)
#Creating a local CSV to view the list
#new_df.to_csv("avengers_movies.csv", index=False)

#Setting up the S3 connection with boto3 --- UNNECESSARY
# s3 = boto3.client("s3")
# bucket_name = "jr-s3-00001" 
# object_name = "avengers_movie_list_01.csv" #S3 destination file name
# file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "avengers_movies.csv") #local filename

# response1 = s3.upload_file(file_name, bucket_name, object_name)
# pprint(response1)  # prints None

try:
    #S3 destination when using airflow inside an EC2
    new_df.to_csv("s3://jr-s3-00001/avengers.csv", sep='\t', index=False)
    print("File uploaded to s3 bucket")
except:
    print("Uh-oh couldn't upload to s3")

#run_itunes_etl()
