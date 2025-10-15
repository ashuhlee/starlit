import os
import sys
import time
import requests
from dotenv import load_dotenv
from typing import Any

from rich.console import Console

from ui.styles import Colors, label

hide_cur = '\033[?25l'
show_cur = '\033[?25h'

console = Console()

# exit app
def exit_app():
    print(hide_cur)
    label('exit', 'Exiting weather-cli..', Colors.pink, False)

    time.sleep(0.5), clear_screen()

    label('exit', 'Exited weather-cli', Colors.pink, False)
    print(show_cur, end='', flush=True)

    sys.exit(0)

# force quit app
def force_quit():
    label('exit', 'Force quitting app', Colors.orange, True)
    sys.exit(0)

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')