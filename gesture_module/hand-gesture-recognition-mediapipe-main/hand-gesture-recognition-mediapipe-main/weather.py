from get_city_from_question import find_location
from bs4 import BeautifulSoup
import requests
import geocoder
from geopy.geocoders import Nominatim
from internet import *;
def getWeather(query):
    if check_internet_connection():
        location = find_location(query)
        
        if len(location) != 0:
            r = requests.get(f"https://www.google.com/search?q=temperature in {location[0]}")
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            return f"temperature in {location[0]} is {temp}"
        else:
            city = getMyCity()
            r = requests.get(f"https://www.google.com/search?q=temperature in {city}")
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            return f"temperature is {temp}"
        
    else:
        return "Check your internet connection!"


def getMyCity():
    ip = geocoder.ip('me').ip

    # Use reverse geocoding to get the city name
    location = geocoder.ip(ip)

    # Extract the city name from the address
    city = location.city

    return city