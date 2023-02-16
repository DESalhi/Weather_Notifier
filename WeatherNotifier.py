import requests
import json
from tkinter import *
import time

# Replace YOUR_API_KEY with your actual API key
API_KEY = "a120cd36c9154d06ab6142705231602"
API_URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q="

def get_weather_data(city):
    url = API_URL + city
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        temp_c = data['current']['temp_c']
        temp_f = data['current']['temp_f']
        condition = data['current']['condition']['text']
        return f"Temperature: {temp_c}°C / {temp_f}°F\nCondition: {condition}"
    else:
        return "Error: Could not retrieve weather data."

def display_notification(city):
    weather_data = get_weather_data(city)
    if weather_data:
        root = Tk()
        root.title("Weather Notification")
        root.geometry("300x100")
        Label(root, text=f"Weather in {city}:").pack()
        Label(root, text=weather_data).pack()
        Button(root, text="Dismiss", command=root.destroy).pack()
        root.mainloop()

while True:
    display_notification("Paris")  # Change the city name here
    time.sleep(60*60)  # Wait for one hour before displaying notification again
