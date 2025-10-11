
from ui.animations import *
from ui.styles import Style, Colors, Misc
from ui.emojis import emoji_map

# console = Console()

def weather_function(city: str) -> bool: # enter a string, return true/false

    complete_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response: requests.Response = requests.get(complete_url)
    data: dict = response.json()

    if data['cod'] != '404':

        spinner('Fetching data...', 1, True)

        city: str = city.title() # get city info
        country_code: str = data['sys']['country'] # get country info

        welcome_message = f'{Style.end}{Style.bold}Welcome to {city}, {country_code}!\n'

        print()
        typewriter(welcome_message, 0.04)
        print(f'- - - - - - - - - - - - - ✈️{Style.end}')

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

        print(f'{Misc.point}Currently: {condition} ({temp} °C)', emoji)
        print(f'{Misc.point}Humidity: {humidity}%')

        if precipitation > 0:
            print(f"{Misc.point}Precipitation: {precipitation}mm ({' + '.join(precip_type)})")
        else:
            print(f'{Misc.point}Precipitation: 0mm (None)')

        return True # city found

    else:
        spinner('Fetching data...', 1, False)
        return False # city not found

# get api key info from .env file
load_dotenv()
api_key: str = os.getenv('API_KEY')

if not api_key:
    print(Style.yellow + 'API Key not found.' + Style.end)
    sys.exit(1)

# print title
clear_screen()
console.print('\n    weather-cli ☀️   ', style='bold #fff8e8 on #7571F9')

# run the main program
while True:
    # using rich package instead of ascii codes
    console.print(f'\n[{Colors.purple} bold]Enter city name: [/bold {Colors.purple}]')

    city_name: str = input(f'{Style.magenta}{Style.bold} {Style.end}')

    if weather_function(city_name):
        # city found → ask if user wants to continue
        while True:
            choice: str = input(f'\n{Style.magenta}Would you like to search another city? (y/n): {Style.end}').lower()

            if choice in ('y', 'yes'):
                break  # break inner loop, continue outer loop for new city

            elif choice in ('n', 'no'):
                # clear_screen()
                print('\nClosing app...')
                sys.exit(0)  # clean exit

            else:
                print("Please enter 'y' or 'n'.")  # prompt again
    else:
        # city not found → ask again (outer loop continues)
        continue
