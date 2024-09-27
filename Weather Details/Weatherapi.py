import requests
from colorama import Fore

city=input("Enter the name of the city to find it's Weather details :")

api_key="8ab22ed87cbabdb732830f7567ff867d"

response=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},IND&appid={api_key}")

a = response.json()[0]

try:
    lat=a['lat']
    lon=a['lon']
except:
    print(f"{city} not found please enter the name of the city properly")
    city = input("Enter the city Name you want to know weather? ")
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},IND&limit=2&appid={api_key}")
    a = response.json()
    
weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}")
weather_detail = weather.json()
print(weather_detail)

print(f"\n{Fore.WHITE}Name : {Fore.GREEN}{city}\n{Fore.WHITE}Weather Description : {Fore.GREEN}{weather_detail['weather'][0]['main']} , {Fore.GREEN}{weather_detail['weather'][0]['description']}\n{Fore.WHITE}Division  : {Fore.GREEN}{weather_detail['name']}\n{Fore.WHITE}Temp (°C) : {Fore.GREEN}{weather_detail['main']['temp']}\n{Fore.WHITE}Feels like (°C): {Fore.GREEN}{weather_detail['main']['feels_like']}\n{Fore.WHITE}Humidity : {Fore.GREEN}{weather_detail['main']['humidity']}")

