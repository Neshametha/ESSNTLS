from Major_Project_Flask import Main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField


class project_location(FlaskForm):
    location = StringField('location')

def yelp_pass(location):
    res = get_yelp_api(location)
    Main_functions.save_to_file(res, "Major_Project_Flask/JSON_Files/Yelp_api.json")

    yelp_json = Main_functions.read_from_file("Major_Project_Flask/JSON_Files/Yelp_api.json")

    yelp_info = yelp_json['businesses']
    for i in yelp_info:
        return (i['name'])


def get_yelp_api(location):

    yelp_url = "https://api.yelp.com/v3/businesses/search"

    yelp_api_key = Main_functions.read_from_file("Major_Project_Flask/JSON_Files/Yelp_key.json")
    my_api_key = yelp_api_key["yelp_key"]
    headers = {'Authorization': 'Bearer %s' % my_api_key}
    params = {'limit': 20, 'categories': '', 'radius': 3000,
              'location': location}
    req1 = requests.get(yelp_url, params=params, headers=headers).json()
    print(req1)

    return req1


def get_google__geocode(latitude, longitude):
    google_url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyAInCy07MuY4BFJL7yZ7xOwIvK0_3j1U-A"
    params = {"lat": latitude, "lng": longitude}

    req = requests.get(google_url, params=params).json()

    Main_functions.save_to_file(req, "Major_Project_Flask/JSON_Files/api.json")

    Main_functions.read_from_file("Major_Project_Flask/JSON_Files/api.json")
    address = req["results"][0]["formatted_address"]
    coordinates = req['results'][0]['geometry']['location']

    return coordinates







