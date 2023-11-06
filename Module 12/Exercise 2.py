
import requests
import json

keyword = input("Enter the municipality: ")
request = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={f3030340c8d510be07322b293eecbb5f}"

response = requests.get(request).json()
print(response)
