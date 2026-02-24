import datetime
import pyjokes
import pywhatkit
import wikipedia
import psutil
import pyautogui
from jarvis_weather import get_weather

def process_command(command):
    command = command.lower()

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return f"The time is {time}"

    elif 'youtube' in command:
        pywhatkit.playonyt("latest video")
        return "Opening YouTube..."

    elif 'who is' in command or 'what is' in command:
        try:
            info = wikipedia.summary(command, sentences=2)
            return info
        except:
            return "Sorry, I couldn't find information on that."

    elif 'joke' in command:
        return pyjokes.get_joke()

    elif 'battery' in command:
        battery = psutil.sensors_battery()
        percent = battery.percent
        return f"Battery is at {percent}%"

    elif 'screenshot' in command:
        pyautogui.screenshot().save("screenshot.png")
        return "Screenshot taken and saved."

    elif 'weather' in command:
        return get_weather("your_city_here")

    elif 'hello' in command:
        return "Hello Ashik! How can I help you today?"

    else:
        return "I'm not sure how to do that yet."