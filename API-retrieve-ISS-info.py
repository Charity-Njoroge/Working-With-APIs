"""
A program that query's a basic API to retrieve data about the
International Space Station (ISS)
"""
import json
import requests


# make a get request to get the latest position of the ISS from the OpenNotify
# API using the iss-now.json  endpoint
response1 = requests.get("http://api.open-notify.org/iss-now.json")
print("The latest position of the International Space Station is \n",
      response1.json())

# make a request to get the next time the ISS will pass over a given location
parameters = {"lat": 37.78, "lon": -122.41}
response2 = requests.get("http://api.open-notify.org/iss-pass.json",
                         params=parameters)
contents = response2.content
# can use the .json() method to return Python object
clean_data = json.loads(contents)
# Get the duration value of the ISS' first pass over San Francisco
#  and assign the value to first_pass_duration.
first_pass_duration = clean_data["response"][0]["duration"]
print("The duration value of the ISS first pass over San Francisco is \n",
      first_pass_duration)
# access the info on how the server generated the data and how to decode it
print(response2.headers)

# get the number of people currently in space using the OpenNotify astros.json
#  endpoint
response3 = requests.get("http://api.open-notify.org/astros.json")
# the content in Python object
contents_astros = response3.json()
# number of people in space
in_space_count = contents_astros["number"]
print("The number of people in space is : ", in_space_count)
