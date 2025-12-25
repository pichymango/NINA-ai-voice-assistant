import requests

API_KEY = "d802eb0cb5cddae0fecedc786b9c09f4"  # put key here

def get_weather(city: str):
    if not city:
        return "Please tell me a city name."

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        r = requests.get(url, timeout=5)
        data = r.json()

        if data.get("cod") != 200:
            return f"I couldn't find weather for {city}"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"The weather in {city} is {desc} with a temperature of {temp}°C"

    except:
        return "I couldn't fetch the weather right now."
