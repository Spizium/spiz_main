import requests
import json

try:
    query = requests.get('https://api.chucknorris.io/jokes/random')
    if query.status_code == 200:
        joke = query.json()
        print(joke['value'])
    else:
        pass
except:
    print("Something went wrongsies oopsies >_<")