#!/usr/bin/env python3

import json
import urllib.request

def get_city():
    with urllib.request.urlopen(' http://ip-api.com/json') as response:
        data = json.loads(response.read())
        return(data["city"],data["countryCode"])


def get_weather(location,output_filename):
    apikey='dac76178c27f507675918ff8d9bc2b95'
    url='http://api.openweathermap.org/data/2.5/weather?q=' + location[0] + ',' + location[1] + '&appid=' + apikey
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    with open(output_filename,'w') as filename:
        filename.write('The weather at ' + location[0] + ' is ' + data["weather"][0]["description"] + "\n")

def main():
    filename="weather.txt"
    location = get_city()
    get_weather(location,filename)



if __name__ == "__main__":
    # execute only if run as a script
    main()
