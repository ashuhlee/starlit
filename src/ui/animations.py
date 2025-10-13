import os
import sys
import time
import requests
from rich.console import Console
from dotenv import load_dotenv

console = Console()

#typewriter effect for text
def typewriter(text: str, speed: float):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

# spinning animation for loading data
def spinner(text: str, speed: float, found):

    print()
    with console.status(f'[cyan]{text}[/cyan]', spinner='dots', spinner_style='magenta'):
        # length of animation
        time.sleep(speed)

    if found:
        console.print('[green]󰄬 Data fetched successfully![/green]')

    elif found is False:
        console.print('[red] City not found. Please try again[/red]')
        time.sleep(0.5)

    elif found is None:
        pass

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# force quit app
def force_quit():
    print('\nForce quitting app.')
    sys.exit(0)