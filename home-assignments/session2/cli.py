#!/usr/bin/env python3

import click
import json
from weather import Weather, Unit

@click.command()
@click.option('--city', prompt='City name', help='The city you need forecast for.')
@click.option('--forecast', prompt='Timeframe for the forecast', help='The timeframe for the forecast.')
@click.option('-c', is_flag=True, help="Will print temperature in Celsius.")
@click.option('-f', is_flag=True, help="Will print temperature in Fahrenheit.")

def main(city,forecast,c,f):
    (weather,temperature_system) = get_weather(c,f)
    forecasts = get_forecasts(weather,city)
    print_forecasts(city,forecast,forecasts,temperature_system)

def print_forecasts(city,forecast,forecasts,temperature_system):
    print("The weather in " + str(city) + \
            " today is " + forecasts[0].text + \
            " with tempratures trailing from " + \
            forecasts[0].low + "-" + forecasts[0].high + " " + temperature_system + ".")

    if forecast != "TODAY":
        num_of_days = int(forecast.split("+")[1])

        print ("\nForecast for the next " + str(num_of_days) + " days:\n")
        for i in range(1,num_of_days + 1):
            print(forecasts[i].date + " " + forecasts[i].text + \
                    " with tempratures trailing from " + \
                    forecasts[i].low + "-" + forecasts[i].high + " " + temperature_system + ".")

def get_forecasts(weather,city):
    city_weather_info=weather.lookup_by_location(str(city))
    forecasts = city_weather_info.forecast
    return(forecasts)

def get_weather(c,f):
    if c:
        weather = Weather(unit=Unit.CELSIUS)
        temperature_system="celsius"
    if f:
        weather = Weather(unit=Unit.FAHRENHEIT)
        temperature_system="fahrenheit"
    return (weather,temperature_system)

if __name__ == '__main__':
    main()

