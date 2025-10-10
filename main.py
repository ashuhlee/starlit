import os, time
import requests, sys
from dotenv import load_dotenv

emoji_map: dict = {
    'Thunderstorm': '⛈️', 'Drizzle': '🌦️', 'Rain': '🌧️', 'Snow': '❄️',
    'Clear': '☀️', 'Clouds': '☁️', 'Mist': '🌫️', 'Smoke': '💨',
    'Haze': '🌫️', 'Dust': '🌪️', 'Fog': '🌫️', 'Sand': '🏜️',
    'Ash': '🌋', 'Squall': '🌬️', 'Tornado': '🌪️'
}

# text styling
BOLD: str = '\033[1m'; END: str = '\033[0m'; YELLOW: str = '\033[33m'; MAGENTA: str = '\033[35m'; GREEN = '\033[32m'

# clears console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

load_dotenv()
api_key: str = os.getenv('API_KEY')

if not api_key:
    print('Error: API Key not found.')
    sys.exit(1)
else:
    print(YELLOW + 'API Key found!' + END)
    time.sleep(1)
    clear_screen()


def weather_function(city: str) -> bool: # enter a string, return true/false

    complete_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response: requests.Response = requests.get(complete_url)
    data: dict = response.json()

    if data['cod'] != '404':

        city: str = city.title() # get city info
        country_code: str = data['sys']['country'] # get country info

        print(f'\n{END}{BOLD}Welcome to {city}, {country_code}!\n- - - - - - - - - - - - - ✈️{END}')

        # temperature + humidity
        getValue: dict = data['main']

        temp: float = getValue['temp'] # get temp (key) matching value
        humidity: int = getValue['humidity'] # get hu
        # humidity (key) matching value

        # get current precipitation
        precipitation: float = 0
        precip_type: list[str] = []

        if 'rain' in data:
            rain: float = data['rain'].get('1h', 0.0)

            precipitation = precipitation + rain
            precip_type.append('Rain') # add rain to [] if rainy

        if 'snow' in data:
            snow: float = data['snow'].get('1h', 0.0)

            precipitation = precipitation + snow
            precip_type.append('Snow') # add snow to [] if snowy

        # weather info
        weather = data['weather'][0] # get weather info
        condition: str = weather['main'] # current condition (clear, snow, clouds...)

        emoji: str

        if condition in emoji_map:
            emoji = emoji_map[condition]
        else:
            emoji = '🌍'

        # change condition naming convention
        if condition == 'Clouds':
            condition = 'Cloudy'

        elif condition == 'Haze':
            condition = 'Hazy'

        print(f'Currently: {condition} ({temp} °C)', emoji)
        print('Humidity:', humidity, '%')

        if precipitation > 0:
            print(f"Precipitation: {YELLOW}{precipitation}mm ({' + '.join(precip_type)}){END}")
        else:
            print(f'Precipitation: {YELLOW}0mm (None){END}')

        return True # city found

    else:
        print('City not found. Please try again')
        return False # city not found

# run the program
while True:

    city_name: str = input(f'Enter city name: {GREEN}')

    if weather_function(city_name):
        # city found → ask if user wants to continue
        while True:
            choice: str = input(f'\n{MAGENTA}Do you want to check another city? (y/n): {END}').lower()

            if choice in ('y', 'yes'):
                print()
                break  # break inner loop, continue outer loop for new city

            elif choice in ('n', 'no'):
                clear_screen()

                print('Exiting program...')
                sys.exit(0)  # clean exit

            else:
                print("Please enter 'y' or 'n'.")  # prompt again
    else:
        # city not found → ask again (outer loop continues)
        continue
