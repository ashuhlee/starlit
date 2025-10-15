from ui.system_utils import *

from ui.animations import *
from ui.styles import Style, Colors, Misc
from ui.emojis import weather_emoji

from core.timezone import get_local_time

def weather_function(city: str) -> bool: # enter a string, return true/false

    complete_url: str = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # loading timer to request data
    fetch_start: float = time.perf_counter()

    response: requests.Response = requests.get(complete_url)
    data: dict = response.json()

    fetch_end: float = time.perf_counter() - fetch_start
    process_time: float = max(fetch_end, 0.5)

    get_code: int = int(data.get('cod', 0))

    error_code: str = f'[bold {Colors.white} on {Colors.red}] Error Code {get_code} [/bold {Colors.white} on {Colors.red}]'
    error_message: str = data.get('message', 'Unknown error')

    # code 200 - city found
    if get_code == 200:
        spinner('Fetching data...', process_time, True)
    # code 404 - city not found
    elif get_code == 404:
        spinner('Fetching data...', process_time, False)
        console.print(f'{error_code} {error_message}')
        return False
    else:
        spinner('Fetching data...', process_time, None)
        # print error type. if error type doesn't exist, print unknown error
        console.print(f'{error_code} {error_message}')
        return False

    city: str = city.title() # get city info
    country_code: str = data['sys']['country'] # get country info

    welcome_message: str = f'Welcome to {city}, {country_code}!\n'

    print()

    text_effect(welcome_message, 1)
    plane_anim()

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

        precipitation: float = precipitation + rain
        precip_type.append('Rain') # add rain to [] if rainy

    if 'snow' in data:
        snow: float = data['snow'].get('1h', 0.0)

        precipitation: float = precipitation + snow
        precip_type.append('Snow') # add snow to [] if snowy

    # weather info
    weather: Any = data['weather'][0] # get weather info
    condition: str = weather['main'] # current condition (clear, snow, clouds...)

    if condition in weather_emoji:
        emoji: str = weather_emoji[condition]
    else:
        emoji: str = '🌍'

    # change condition naming convention
    if condition == 'Clouds':
        condition = 'Cloudy'

    elif condition == 'Haze':
        condition = 'Hazy'

    elif condition == 'Rain':
        condition = 'Rainy'

    curr_weather: str = f'{Misc.point}Currently: {condition} ({temp} °C) {emoji}'
    curr_hum: str = f'{Misc.point}Humidity: {humidity}%'

    precip_status: str = f"{Misc.point}Precipitation: {precipitation}mm ({' + '.join(precip_type)})"
    precip_status_none: str = f'{Misc.point}Precipitation: 0mm (None)'

    # temperature + humidity
    print(curr_weather, curr_hum, precip_status if precipitation > 0 else precip_status_none, sep='\n')

    # timezone
    curr_timezone: str = get_local_time(data['timezone'])
    console.print(f'\n🕓 [bold]Local time: {curr_timezone}[/bold]')

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

    city_name: str = input(f'{Misc.user_input}')

    if city_name.lower() in ('q', 'quit'):
        force_quit()

    if weather_function(city_name):
        # city found → ask if user wants to continue
        while True:
            choice = console.input(
                f'\n[bold {Colors.purple}]Explore another forecast?[/bold {Colors.purple}] [magenta] [/magenta]').lower()

            if choice.lower() in ('y', 'yes'):
                break  # start new search

            elif choice.lower() in ('n', 'no'):
                exit_app()

            elif choice.lower() in ('q', '-q', '--quit', 'quit'):
                force_quit()

            else:
                label("warn", "Please enter 'y' or 'n' ", Colors.orange, True)  # prompt again
    else:
        # city not found → ask again (outer loop continues)
        continue
