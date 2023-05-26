import requests
import json
import time
from tkinter import Tk, Label, Button

# Replace YOUR_API_KEY with your actual API key
API_KEY = "a120cd36c9154d06ab6142705231602"
API_URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q="

class WeatherNotifier:
    def __init__(self, city, interval):
        self.city = city
        self.interval = interval

    def get_weather_data(self):
        url = API_URL + self.city
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = json.loads(response.content)
            temp_c = data['current']['temp_c']
            temp_f = data['current']['temp_f']
            condition = data['current']['condition']['text']
            return f"Temperature: {temp_c}°C / {temp_f}°F\nCondition: {condition}"
        except requests.exceptions.RequestException as e:
            return f"Error: Could not retrieve weather data. {str(e)}"

    def display_notification(self):
        weather_data = self.get_weather_data()
        if weather_data:
            root = Tk()
            root.title("Weather Notification")
            root.geometry("300x100")

            # Get the screen width and height
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()

            # Calculate the position for the bottom right corner
            window_width = 300
            window_height = 100
            x = screen_width - window_width - 10  # 10 pixels offset from the right edge
            y = screen_height - window_height - 80  # 10 pixels offset from the bottom edge

            # Set the window position
            root.geometry(f"{window_width}x{window_height}+{x}+{y}")

            Label(root, text=f"Weather in {self.city}:").pack()
            Label(root, text=weather_data).pack()
            Button(root, text="Dismiss", command=root.destroy).pack()
            root.mainloop()

    def run(self):
        while True:
            self.display_notification()
            time.sleep(self.interval)

if __name__ == "__main__":
    city_name = "Paris"  # Change the city name here
    interval_seconds = 60 * 60  # Change the interval time in seconds here
    notifier = WeatherNotifier(city_name, interval_seconds)
    notifier.run()
