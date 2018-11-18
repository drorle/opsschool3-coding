#!/usr/bin/env python3

import json
import urllib.request

OUTPUT_FILE="weather.txt"
APIKEY='dac76178c27f507675918ff8d9bc2b95'

def get_city():
    with urllib.request.urlopen(' http://ip-api.com/json') as response:
        data = json.loads(response.read())
        return(data["city"],data["countryCode"])


def get_weather(location,output_filename):
    url='http://api.openweathermap.org/data/2.5/weather?q=' + location[0] + ',' + location[1] + '&appid=' + APIKEY
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    with open(output_filename,'a') as filename:
        filename.write('The weather at ' + location[0] + ' is ' + data["weather"][0]["description"] + "\n")

def get_weather_for_multiple_cities(city_list):
    for city in city_list:
        location = [city,"IL"]
        get_weather(location,OUTPUT_FILE)

def main():
    location = get_city()
    get_weather(location,OUTPUT_FILE)
    get_weather_for_multiple_cities(["Ashkelon","Jerusalem","Tel Aviv","Haifa","Raanana","Eilat","Carmiel","Holon","Ashdod","Ramat Gan"])



if __name__ == "__main__":
    # execute only if run as a script
    main()
