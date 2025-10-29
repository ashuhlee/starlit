import random
import time
import requests
import sys
import re
import os
from dotenv import load_dotenv
from pathlib import Path


env_file = Path.home() / ".config" / "starlit" / ".env"
load_dotenv(env_file)

# check if string color is a valid hex code
def is_valid_hex(color: str) -> bool:
    return bool(re.fullmatch(r'[0-9A-Fa-f]{6}', color))

def make_valid_hex(color: str, default: str):

    if is_valid_hex(color):
        return f'#{color}'
    else:
        return f'#{default}'


DEFAULT_1_TTE = '7571F9'
DEFAULT_2_TTE = 'F7A4F4'

color1_tte: str = os.getenv("COLOR_1", DEFAULT_1_TTE)
color2_tte: str = os.getenv("COLOR_2", DEFAULT_2_TTE)

DEFAULT_1_RICH = '7571F9'
DEFAULT_2_RICH = 'F7A4F4'

color1_rich: str = os.getenv("COLOR_1", DEFAULT_1_RICH)
color2_rich: str = os.getenv("COLOR_2", DEFAULT_2_RICH)