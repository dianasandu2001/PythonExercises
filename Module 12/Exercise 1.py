import requests
import json


request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request).json()
    print(response["value"])
except:
    print("Error")