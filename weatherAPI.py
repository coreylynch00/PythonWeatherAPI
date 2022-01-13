from pprint import pprint
import requests

URL = ("http://api.openweathermap.org/data/2.5/weather?q=")
API_KEY = ("&APPID=a96ce88fe9d17f75eb44312d7aab6d5c")
location = ""

while location != "Q":
    location = input("City Name ('Q' to Quit): ")
    if location == "Q":
        print("\nGoodbye!")
        exit(0)
    else:
        r = requests.get(URL+location+API_KEY)
        print(f"\nWeather for {location}:")
        pprint(r.json())
        print("\n")