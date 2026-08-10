import requests


OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f1b52c81116a7b428be5e081ee3b04a8"

weather_params = {
    "lat":8.980603,
    "lon":38.757759,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    print("Bring an Umbrela")

