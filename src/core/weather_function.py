from ui.animations import *
from ui.graphics import *
from ui.styles import Colors, label, gradient_text

from core.timezone import *
from core.wind_direction import wind_arrow

load_dotenv()

API_KEY = os.getenv('API_KEY')
UNITS = os.getenv('UNITS', 'metric')

DISABLE_ANIMATION = os.getenv('DISABLE_ANIMATION', 'false')

SHOW_DT = os.getenv('SHOW_DT', 'true')
SHOW_ASCII = os.getenv('SHOW_ASCII', 'true')
SHOW_MSG = os.getenv('SHOW_MSG', 'true')

SHOW_EMOJI = os.getenv('SHOW_EMOJI', 'true')
EMOJI_TYPE = os.getenv('EMOJI_TYPE', '🐻')


def weather_function(city: str):  # enter a string, return true/false

    # set city, api key + unit of measurement
    complete_url: str = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={UNITS}'

    # loading timer to request data
    fetch_start: float = time.perf_counter()

    response: requests.Response = requests.get(complete_url)
    data: dict = response.json()

    fetch_end: float = time.perf_counter() - fetch_start
    process_time: float = max(fetch_end, 0.25)

    # get response code
    get_code: int = int(data.get('cod', 0))

    error_code: str = f'[bold {Colors.white} on {Colors.red}] Error {get_code} [/bold {Colors.white} on {Colors.red}]'
    error_message: str = data.get('message', 'Unknown error').lower() # if error type doesn't exist, print unknown error

    # code 200 - city found
    if get_code == 200:
        spinner('Fetching data...', process_time, True)
    # code 404 - city not found
    elif get_code == 404:
        spinner('Fetching data...', process_time, False)
        console.print(f'{error_code} {error_message}')
        return False
    # code 401 - invalid api key
    elif get_code == 401:
        spinner('Fetching data...', process_time, False)
        console.print(f'{error_code} {error_message}')
        return False
    else:
        spinner('Fetching data...', process_time, None)
        console.print(f'{error_code} {error_message}') # print error type
        return False

    getSys: dict = data.get('sys', {})

    city: str = city.title()  # get city info
    country_code: str = getSys.get('country')  # get country info

    # weather info
    weather = data['weather'][0]  # get weather info
    condition: str = weather['main']  # current condition (clear, snow, clouds...)

    # current time + date
    curr_timezone: str = get_local_time(data['timezone'])
    curr_date: str = get_local_date(data['timezone'])

    # sunrise + sunset
    sunrise: int = getSys.get('sunrise', 0)
    sunset: int = getSys.get('sunset', 0)

    # wind speed + degree
    getWind: dict = data.get('wind', {})

    wind_deg: int = getWind.get('deg', 0)
    wind_dir: str = wind_arrow(wind_deg)

    wind_speed: float = getWind.get('speed', 0.0)

    if UNITS.lower() == 'metric':
        wind_val: float = round(wind_speed * 3.6, 1)
        wind_unit = 'km/h'

    elif UNITS.lower() == 'imperial':
        wind_val: float = round(wind_speed, 1)
        wind_unit = 'mph'

    else:
        wind_val: float = round(wind_speed * 3.6, 1)
        wind_unit = 'km/h' # defaults to metric

    # temperature + humidity
    getValue: dict = data['main']

    temp: float = getValue['temp']  # get temp (key) matching value
    humidity: int = getValue['humidity']  # get hu

    # get current precipitation
    precipitation: float = 0
    precip_type: list[str] = []

    if 'rain' in data:
        rain: float = data['rain'].get('1h', 0.0)

        precipitation: float = precipitation + rain
        precip_type.append('Rain')  # add rain to [] if rainy

    if 'snow' in data:
        snow: float = data['snow'].get('1h', 0.0)

        precipitation: float = precipitation + snow
        precip_type.append('Snow')  # add snow to [] if snowy


    if condition in weather_emoji:
        emoji: str = weather_emoji[condition]
    else:
        emoji: str = ''

    # show emoji config #1

    if SHOW_EMOJI.lower() == 'true':
        welcome_message: str = f'Forecast for {city}, {country_code} {emoji}\n'

    elif SHOW_EMOJI.lower() == 'false':
        welcome_message: str = f'Forecast for {city}, {country_code}\n'

    else:
        welcome_message: str = f'Forecast for {city}, {country_code} {emoji}\n' # print emoji by default

    # print welcome message

    if DISABLE_ANIMATION.lower() == 'true':
        time.sleep(0.2)
        gradient_text(welcome_message)

    elif DISABLE_ANIMATION.lower() == 'false':
        text_effect(welcome_message, 1)

    else:
        text_effect(welcome_message, 1) # fallback: animate

    # formatted info to print
    precip_status: str = f"precip   {Misc.divider}  {precipitation}mm ({' + '.join(precip_type).lower()})"
    precip_status_none: str = f'precip   {Misc.divider}  0mm | 0%'

    sun_event: str = get_sun_time(sunrise, sunset, data['timezone'])

    curr_hum: str = f'humidity {Misc.divider}  {humidity}%'

    curr_precip = precip_status if precipitation > 0 else precip_status_none
    curr_wind: str = f'wind     {Misc.divider}  {wind_val} {wind_unit} {wind_dir}'

    # show ascii configs

    if SHOW_ASCII.lower() == 'true':
        display_ascii(condition, temp, sun_event, curr_wind, curr_hum, curr_precip)

    elif SHOW_ASCII.lower() == 'false':
        display_ascii(condition, temp, sun_event, curr_wind, curr_hum, curr_precip, False)

    else:
        display_ascii(condition, temp, sun_event, curr_wind, curr_hum, curr_precip) # fallback: display art


    # show date time config

    if SHOW_DT.lower() == 'true':
        print(f'\n{curr_date}  {curr_timezone}') # print local date + time

    elif SHOW_DT.lower() == 'false':
        pass

    else:
        print(f'\n{curr_date}  {curr_timezone}') # fallback: show date time

    if condition in weather_msg:
        suggestion = random.choice(weather_msg[condition])
    else:
        suggestion = 'have a great day today :]'

    # show emoji config

    if SHOW_EMOJI.lower() == 'true':
        msg_emoji = EMOJI_TYPE
    elif SHOW_EMOJI.lower() == 'false':
        msg_emoji = ''
    else:
        msg_emoji = '🐻'

    space = ' ' if msg_emoji else ''

    # label configs
    if SHOW_MSG.lower() == 'true':
        label(f'{msg_emoji}{space}msg', suggestion, Colors.custom_label, True)

    elif SHOW_MSG.lower() == 'false':
        pass
    else:
        label(f'{weather_emoji} msg', suggestion, Colors.custom_label, True) # fallback: show message

    print_warnings()
    return True  # city found
