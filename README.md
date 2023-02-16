# Weather_Notifier
Weather Notifier is a Python package that allows you to receive desktop notifications with the current weather conditions for a specified city. With just a few lines of code, you can get up-to-date weather information without having to constantly check a weather website or app.

Weather Notifier uses the WeatherAPI to get weather data. To use WeatherAPI, you will need to sign up for a free API key on their website. Once you have your API key, you can easily integrate Weather Notifier into your Python project and start receiving weather notifications in real time.

Whether you're planning a trip, monitoring weather conditions for outdoor activities, or just want to stay informed about the weather in your area, Weather Notifier makes it easy to get the information you need. Install Weather Notifier today and start receiving desktop notifications with the latest weather data.

## Usage
To use Weather Notifier, simply import the package and call the display_notification function with the name of the city you want to get the weather for:
```
from WeatherNotifier import display_notification
display_notification("Paris")
```
This will display a desktop notification with the current weather conditions for Paris.

By default, WeatherNotifier will display notifications once an hour. If you want to change the frequency, you can modify the time.sleep value in the while loop in the WeatherNotifier.py file.

## API key
Weather Notifier uses the WeatherAPI to get weather data. To use WeatherAPI, you will need to sign up for a free API key on their website. Once you have your API key, you can replace the API_KEY variable in the WeatherNotifier.py file with your actual API key.

## Contributing
If you find a bug or have a suggestion for a new feature, feel free to open an issue or submit a pull request. We welcome contributions from anyone.

## License
Weather Notifier is licensed under the MIT license.

