import requests
import json
import pprint as pp

headers = {
    'User-Agent': 'S-Lehtonen, Metropolia AMK',
    'User-type' : 'Student',
    'From': 'https://github.com/Spizium'
}

def PlaceQeury(munc):
    target = munc
    target = target.replace(' ', ',')
    url = f'https://nominatim.openstreetmap.org/search?q={target}&format=geojson'
    request = requests.get(url, headers=headers)
    text = request.json()
    return text['features'][0]['geometry']['coordinates']

def WeatherQuery(coords):
    url = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={coords[0]}&lon={coords[1]}&altitude=4150'
    request = requests.get(url, headers=headers)
    text = request.json()
    return text

def PrintInfo(data):
    weather_type = data['properties']['timeseries'][0]['data']['next_1_hours']['summary']['symbol_code']
    dataset =  data['properties']['timeseries'][0]['data']['instant']['details']
    temp =  dataset['air_temperature']
    humi = dataset['relative_humidity']
    cloud_cover = dataset['cloud_area_fraction']
    wind_spd = dataset['wind_speed']
    wind_drct = dataset['wind_from_direction']
    print(f"Weather:        {weather_type}")
    print(f"Temperature:    {temp} °C")
    print(f"Humidity:       {humi} %")
    print(f"Cloud cover:    {cloud_cover} %")
    print(f"Wind speed:     {wind_spd} m/s")
    print(f"Wind direction: {wind_drct}")

user_input = input("Enter municipality name: ")
Coordinates = PlaceQeury(user_input)
data = WeatherQuery(Coordinates)
PrintInfo(data)