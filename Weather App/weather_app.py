import requests
import json

city = input("Enter your city name:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=e980ac2892c543c89bd64822230204&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])