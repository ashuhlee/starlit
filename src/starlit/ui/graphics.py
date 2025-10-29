from starlit.ui.styles import Misc
from starlit.ui.helpers import *


weather_ascii: dict = {

    'Clouds': [
        r"",
        r"               {weather}",
        r"    .--.      {sun}",
        r"  .-(    ).    {wind}",
        r" (___.__)__)   {humidity}",
        r"               {precip}",
    ],

    'Rain': [
        r"",
        r"    .--.      {weather}",
        r"  .-(    ).    {sun}",
        r" (___.__)__)   {wind}",
        r"  ‚'‚'‚'‚'     {humidity}",
        r"               {precip}",
    ],

    'Drizzle': [
        r"",
        r"    .--.      {weather}",
        r"  .-(    ).    {sun}",
        r" (___.__)__)   {wind}",
        r"   ' ' ' '     {humidity}",
        r"               {precip}",
    ],

    'Thunderstorm': [
        r"",
        r"    .--.      {weather}",
        r"  .-(    ).    {sun}",
        r" (___.__)__)   {wind}",
        r" ,',' 󱐋 ,','   {humidity}",
        r"               {precip}",
    ],

    'Snow': [
        r"",
        r"  .+ .--.      {weather}",
        r"  .-(    ).    {sun}",
        r" (___.__)__)   {wind}",
        r" . * . * .*    {humidity}",
        r"  ---------    {precip}",
    ],

    'Fog': [
        r"",
        r"  . _ - _       {weather}",
        r" _ - _ - _ -    {sun}",
        r"  _ - _ - _     {wind}",
        r" _ . _ - . -    {humidity}",
        r"                {precip}",
    ],

    'Mist': [
        r"",
        r"  . _ - _ .     {weather}",
        r" _ - _ . _ -    {sun}",
        r"  _ - _ - _     {wind}",
        r" _ . _ - . -    {humidity}",
        r"                {precip}",
    ],

    'Haze': [
        r"",
        r"  . _ - _ .     {weather}",
        r" _ - .--. -     {sun}",
        r"_ .-(    ).-    {wind}",
        r" (___.__)__)    {humidity}",
        r"                {precip}",
    ],

    'Clear': [
        r"",
        r"    ⸜    ⸝     {weather}",
        r"    .—.       {sun}",
        r"  ‒ (   ) ‒    {wind}",
        r"     `—᾿       {humidity}",
        r"    ⸍    ⸌     {precip}",
    ],

}

default_ascii: list = [
        r"",
        r"               {weather}",
        r"    .--.      {sun}",
        r"  .-(    ).    {wind}",
        r" (___.__)__)   {humidity}",
        r"               {precip}",
]

no_ascii: list = [
    r'',
    r'{weather}',
    r'{sun}',
    r'{wind}',
    r'{humidity}',
    r'{precip}',
    ]


weather_msg: dict = {

    'Thunderstorm': ["yeah, you're gonna need an umbrella.",
                     "hope you like lightning!",
                     "you're not afraid of thunder right?"],

    'Drizzle': ['perhaps an umbrella?'],

    'Rain': ['might want to grab an umbrella',
             'take that umbrella (please)',
             'you have an umbrella, right?'],

    'Snow': ['alexa play santa tell me',
             'you might meet mariah carey'],

    'Clear': ['perfect, go touch some grass',
              'ooooh, the sun!',
              'the sun misses you btw',
              'hope you have a great day!'],

    'Clouds': ['a chill playlist kinda day',
               "aw, where's the sun?"],

    'Mist': ['feels kind of dreamy'],

    'Smoke': ['maybe keep the windows closed',
              '*coughs*'],

    'Haze': ['its a lil hazy, stay safe'],
    'Dust': ['close your windows, okay?'],

    'Fog': ['drive safe and stay warm!',
            'in my restless dreams, i see that town. silent hill'],

    'Sand': ['stay hydrated :]'],
    'Ash': ['uh...stay home today'],
    'Squall': ['keep the hat at home'],

    'Tornado': ['uh...stay home today',
                'dont. go. outside.']
}


weather_emoji: dict = {

    'Thunderstorm': '⛈️',
    'Drizzle': '🌦️',
    'Rain': '🌧️',
    'Snow': '❄️',
    'Clear': '☀️',
    'Clouds': '☁️',
    'Mist': '🌫️',
    'Smoke': '💨',
    'Haze': '🌫️',
    'Dust': '🌪️',
    'Fog': '🌫️',
    'Sand': '🏜️',
    'Ash': '🌋',
    'Squall': '🌬️',
    'Tornado': '🌪️'
}

condition_labels: dict = {
    'Clouds': 'Cloudy',
    'Haze': 'Hazy',
    'Clear': 'Clear Sky',
    'Rain': 'Rainy',
    'Snow': 'Snowy',
    'Mist': 'Misty',
    'Fog': 'Foggy'
}


UNITS = os.getenv('UNITS', 'metric')

# change condition names
def better_conditions(condition: str) -> str:

    # return new condition, if it doesn't exist, return the default condition
    return condition_labels.get(condition, condition)

def display_ascii(condition: str, temp: float, sun: str, wind: str, humidity: str, precip: str, show_ascii: bool = True):

    new_condition = better_conditions(condition)
    ascii_art = weather_ascii.get(condition, default_ascii) if show_ascii else no_ascii

    if UNITS.lower() == 'metric':
        temp_unit = '°C'
    elif UNITS.lower() == 'imperial':
        temp_unit = '°F'
    else:
        temp_unit = '°C' # defaults to metric

    pretty_weather: str = f'weather  {Misc.divider}  {new_condition.lower()} ({round(temp, 1)}{temp_unit})'

    for line in ascii_art:
        print(line.format(weather = pretty_weather, sun = sun, wind = wind, humidity = humidity, precip = precip))

