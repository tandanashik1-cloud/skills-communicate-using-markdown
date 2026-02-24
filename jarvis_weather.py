import requests

def get_weather(city):
    api_key = "YOUR_OPENWEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return "City not found."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return f"{city.title()} weather: {weather}, {temp}°C (feels like {feels_like}°C), humidity: {humidity}%"

    except Exception as e:
        return f"Error fetching weather: {e}"