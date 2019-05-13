import os
from typing import Dict, List, Any
import requests
from mypy_extensions import TypedDict
from secret import api_key
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

Weather = TypedDict('Weather', {
    'main': str,
    'description': str,
    'temp': float,
    'humidity': float,
    'temp_min': float,
    'temp_max': float
})

res: Any = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q=Amsterdam&APPID={API_KEY}').json()


weather: Weather = {
    'main': res['weather'][0]['main'],
    'description': res['weather'][0]['description'],
    'temp': res['main']['temp'],
    'humidity': res['main']['humidity'],
    'temp_min': res['main']['temp_min'],
    'temp_max': res['main']['temp_max']
}

print(weather['description'])
