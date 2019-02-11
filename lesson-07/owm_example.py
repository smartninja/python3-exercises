import json
from urllib.request import urlopen

api_key = "b1b15e88fa797225412429c1c50c122a1"  # insert your own API key!!!

response = urlopen('http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=' + api_key).read()

data = json.loads(response)  # in case you get error, try utf-8: data = json.loads(response.decode('utf-8'))

print(data)
print(data["weather"][0]["description"])
