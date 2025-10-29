
from starlit.ui.helpers import *
from starlit.ui.styles import Colors, label, gradient_text

from starlit.ui.animations import spinner, text_effect
from starlit.ui.graphics import weather_msg, weather_emoji, display_ascii

from starlit.core.timezone import *
from starlit.core.wind_direction import wind_arrow

from starlit.utils.system_utils import print_warnings


api_key = os.getenv('API_KEY')
units = os.getenv('UNITS', 'metric')

disable_anim = os.getenv('DISABLE_ANIMATION', 'false')

show_dt = os.getenv('SHOW_DT', 'true')
show_ascii = os.getenv('SHOW_ASCII', 'true')
show_msg = os.getenv('SHOW_MSG', 'true')

show_emoji = os.getenv('SHOW_EMOJI', 'true')
emoji_type = os.getenv('EMOJI_TYPE', '🐻')


def weather_function(city: str):  # enter a string, return true/false

    # set city, api key + unit of measurement
    complete_url: str = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'

    # loading timer to request data
    fetch_start: float = time.perf_counter()

    response: requests.Response = requests.get(complete_url)
    data: dict = response.json()

    fetch_end: float = time.perf_counter() - fetch_start
    process_time: float = max(fetch_end, 0.2)

    # get response code
    get_code: int = int(data.get('cod', 0))
    error_msg: str = data.get('message', 'Unknown error') # if error type doesn't exist, print unknown error

    # code 200 - city found
    if get_code == 200:
        spinner('Fetching data...', process_time, True, disable_anim.lower() != 'true')

    # code 404 - city not found
    elif get_code == 404:
        spinner('Fetching data...', process_time, False, disable_anim.lower() != 'true')
        label(f'Error {get_code}', error_msg, Colors.red, False)
        return False

    # code 401 - invalid api key
    elif get_code == 401:
        spinner('Fetching data...', process_time, False, disable_anim.lower() != 'true')
        label(f'Error {get_code}', error_msg, Colors.red, False)
        sys.exit(1)

    else:
        spinner('Fetching data...', process_time, None, disable_anim.lower() != 'true')
        label(f'Error {get_code}', error_msg, Colors.red, False) # print error type
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

    # set unit types
    if units.lower() == 'metric':
        wind_val: float = round(wind_speed * 3.6, 1)
        wind_unit = 'km/h'

    elif units.lower() == 'imperial':
        wind_val: float = round(wind_speed, 1)
        wind_unit = 'mph'

    else:
        wind_val: float = round(wind_speed * 3.6, 1)
        wind_unit = 'km/h' # fallback: metric

    # temperature + humidity
    getValue: dict = data['main']

    temp: float = getValue['temp']  # get temp (key) matching value
    humidity: int = getValue['humidity']  # get humidity (key) matching value

    # get current precipitation
    precipitation: float = 0
    precip_type: list = []

    if 'rain' in data:
        rain: float = data['rain'].get('1h', 0.0)

        precipitation: float = precipitation + rain
        precip_type.append('Rain')  # add rain to [] if rainy

    if 'snow' in data:
        snow: float = data['snow'].get('1h', 0.0)

        precipitation: float = precipitation + snow
        precip_type.append('Snow')  # add snow to [] if snowy

    # add matching emoji to location title
    if condition in weather_emoji:
        emoji: str = weather_emoji[condition]
    else:
        emoji: str = ''

    # show emoji config #1
    if show_emoji.lower() == 'true':
        welcome_message: str = f'Forecast for {city}, {country_code} {emoji}\n'

    elif show_emoji.lower() == 'false':
        welcome_message: str = f'Forecast for {city}, {country_code}\n'

    else:
        welcome_message: str = f'Forecast for {city}, {country_code} {emoji}\n' # fallback: show emoji

    # print welcome message
    if disable_anim.lower() == 'true':
        time.sleep(0.1)
        gradient_text(welcome_message)

    elif disable_anim.lower() == 'false':
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
    if show_ascii.lower() == 'true':
        display_ascii(condition, temp, sun_event, curr_wind, curr_hum, curr_precip)

    elif show_ascii.lower() == 'false':
        display_ascii(condition, temp, sun_event, curr_wind, curr_hum, curr_precip, False)

    else:
        display_ascii(condition, temp, sun_event, curr_wind, curr_hum, curr_precip) # fallback: display art

    # show date time config
    if show_dt.lower() == 'true':
        print(f'\n{curr_date}  {curr_timezone}') # print local date + time

    elif show_dt.lower() == 'false':
        pass

    else:
        print(f'\n{curr_date}  {curr_timezone}') # fallback: show date time

    # display message at the bottom
    if condition in weather_msg:
        suggestion = random.choice(weather_msg[condition])
    else:
        suggestion = 'have a great day today :]'

    # show emoji config
    if show_emoji.lower() == 'true':
        msg_emoji = emoji_type
    elif show_emoji.lower() == 'false':
        msg_emoji = ''
    else:
        msg_emoji = emoji_type

    space = ' ' if msg_emoji else ''

    # label configs
    if show_msg.lower() == 'true':
        label(f'{msg_emoji}{space}msg', suggestion, Colors.custom_label, True)

    elif show_msg.lower() == 'false':
        pass
    else:
        label(f'{weather_emoji} msg', suggestion, Colors.custom_label, True) # fallback: show message

    print_warnings()
    # label('TEST', f'fetched in [cyan]{round((fetch_end * 1000), 2)}ms[/cyan]', Colors.title, True)
    return True  # city found
