import requests
from datetime import datetime

from config.config import Config, load_config


def get_data(city, latitude, longitude):
    config: Config = load_config()

    url = (f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}'
           f'&lon={longitude}&appid={config.openweathermap_key}&lang=ru&units=metric')

    if city:
        url = (f'https://api.openweathermap.org/data/2.5/weather?q={city},'
               f'ru&appid={config.openweathermap_key}&lang=ru&units=metric')

    return requests.get(url).json()


def get_weather(city=None, latitude=None, longitude=None):
    data = get_data(city, latitude, longitude)

    if data['cod'] != 200:
        return 'Населенный пункт не найден ☹'

    city = data['name']
    current_temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
    sunset = datetime.fromtimestamp(data['sys']['sunset'])

    return (f'{city}\nТемпература: {current_temp} °C 🌡\nВлажность: {humidity}% 💧\nСкорость ветра: {wind} м/с 💨\n'
            f'Восход: {sunrise} 🌅\nЗакат: {sunset} 🌇')
