# services/weather.py

import requests

API_KEY = "78d5e96c776280b01304755779a2d4bb"


def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url, timeout=5)
        data = res.json()

        temp = data["main"]["temp"]

        if temp < 10:
            return "Winter"
        elif temp > 28:
            return "Summer"
        return "Moderate"

    except:
        return "Moderate"