from ui.animations import *
from ui.styles import Style, Colors, Misc
from ui.emojis import emoji_map


def weather_function(city: str) -> bool: # enter a string, return true/false

    complete_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response: requests.Response = requests.get(complete_url)
    data: dict = response.json()

    get_code = int(data.get('cod', 0))

    error_code = f'[bold {Colors.white} on {Colors.red}] Error Code {get_code} [/bold {Colors.white} on {Colors.red}]'
    error_message = data.get('message', 'Unknown error')

    # code 200 - city found
    if get_code == 200:
        spinner('Fetching data...', 1, True)
    # code 404 - city not found
    elif get_code == 404:
        spinner('Fetching data...', 1, False)
        return False
    else:
        spinner('Fetching data...', 1, None)
        # print error type. if error type doesn't exist, print unknown error
        console.print(f'{error_code} {error_message}')
        return False

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

# get api key info from .env file
load_dotenv()
api_key: str = os.getenv('API_KEY')

# print title
clear_screen()
console.print('\n  WEATHER CLI ☀️ ', style=f'bold {Colors.white} on {Colors.title}')

# run the main program
while True:
    # using rich package instead of ascii codes
    console.print(f'\n[bold {Colors.purple}]Enter city name: [/bold {Colors.purple}]')

    city_name: str = input(f'{Style.magenta}{Style.bold} {Style.end}')

    if city_name.lower() in ('q', '-q', '--q', 'quit'):
        force_quit()

    if weather_function(city_name):
        # city found → ask if user wants to continue
        while True:
            choice: str = input(f'\n{Style.magenta}Would you like to search another city? (y/n): {Style.end}').lower()

            if choice.lower() in ('y', 'yes'):
                break  # break inner loop, continue outer loop for new search

            elif choice.lower() in ('n', 'no'):
                # clear_screen()
                console.print('\nClosing weather forecast app...', style='bold')
                sys.exit(0)  # clean

            elif choice.lower() in ('q', '-q', '--q', 'quit'):
                force_quit()

            else:
                console.print(f"\n[bold {Colors.white} on {Colors.orange}] WARN [/bold {Colors.white} on {Colors.orange}] Please enter 'y' or 'n'.")  # prompt again
    else:
        # city not found → ask again (outer loop continues)
        continue
