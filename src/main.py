# this file handles all the flags

import os
import argparse
from ui.styles import label, Colors, Console, load_dotenv
from core.weather_function import weather_function
from interactive_mode import interactive_mode

load_dotenv()
console = Console()

API_KEY = os.getenv('API_KEY')
DEFAULT_CITY = os.getenv("DEFAULT_CITY", None)

UNITS = os.getenv('UNITS', 'Default')
DISABLE_ANIMATION = os.getenv('DISABLE_ANIMATION', 'Default')
SHOW_DT = os.getenv('SHOW_DT', 'Default')
SHOW_ASCII = os.getenv('SHOW_ASCII', 'Default')
SHOW_MSG = os.getenv('SHOW_MSG', 'Default')
SHOW_EMOJI = os.getenv('SHOW_EMOJI', 'Default')
EMOJI_TYPE = os.getenv('EMOJI_TYPE', 'Default')

COLOR_1 = os.getenv('COLOR_1', 'Default')
COLOR_2 = os.getenv('COLOR_2', 'Default')
LABEL_COLOR = os.getenv('LABEL_COLOR', 'Default')

VERSION = "0.1.0"

def main():
    parser = argparse.ArgumentParser(
        prog="starlit",
        description="starlit weather cli 🐻"
    )

    # optional positional argument for city (default if none)
    parser.add_argument("city", nargs="?",
        help="City name to fetch weather for"
    )

    # runs interactive mode
    parser.add_argument("-i", "--interactive",
        action="store_true",
        help="Start interactive mode"
    )

    # version
    parser.add_argument("-v", "--version",
        action="store_true",
        help="Show the version"
    )

    # views config in terminal
    parser.add_argument("-c", "--config",
        action="store_true",
        help="View config settings in console"
    )

    parser.add_argument("--show-full",
        action="store_true",
        help="Show full config file contents"
    )

    # opens config file in editor
    parser.add_argument("-e", "--edit",
        action="store_true",
        help="Open config file for editing")

    args = parser.parse_args()

    # open config file in default editor
    if args.edit:
        env_path = ".env"

        if os.path.exists(env_path):
            editor = os.getenv("EDITOR", "nano")
            os.system(f"{editor} {env_path}")
        else:
            label('ERROR',
                  'No .env file found to edit',
                  Colors.red, True)
        return

    # print version
    if args.version:
        print(f"starlit version {VERSION}")
        return

    # run interactive mode
    if args.interactive:
        interactive_mode()
        return

    # display config settings
    if args.config:
        env_path = ".env"
        api_key_length = 32

        if os.path.exists(env_path):

            label('.ENV','[bold]starlit config[/bold]\n', Colors.dark_pink_2, True)

            if not args.show_full:

                print("API Settings:")
                console.print(f"  └─ API Key: {"[green]Connected[/green]" if API_KEY and len(API_KEY.strip()) == api_key_length 
                else '[red]Not Connected[/red]'}")

                values = {"true": "Yes", "false": "No"}

                print("\nDisplay Settings:")
                print(f"  ├─ Default City: {DEFAULT_CITY.capitalize()}")
                print(f"  ├─ Units: {UNITS.capitalize()}")

                print(f"  ├─ Show Date & Time: {values.get(SHOW_DT.lower(), "Yes")}")
                print(f"  ├─ Show Ascii: {values.get(SHOW_ASCII.lower(), "Yes")}")
                print(f"  ├─ Show Message: {values.get(SHOW_MSG.lower(), "Yes")}")

                print(f"  ├─ Show Emojis: {values.get(SHOW_EMOJI.lower(), "Yes")}")
                print(f"  └─ Emoji Type: {EMOJI_TYPE}")

                print("\nColor Settings:")

                print(f"  ├─ Color 1: {COLOR_1}")
                print(f"  ├─ Color 2: {COLOR_2}")
                print(f"  └─ Label Color: {LABEL_COLOR}")

            else:

                with open(env_path, "r", encoding="utf-8") as f:

                    for line in f:
                        strip = line.strip()

                        # hide api key in terminal
                        if strip.startswith("API_KEY="):
                            if API_KEY and len(API_KEY.strip()) == api_key_length:
                                console.print("API_KEY: [green]Connected[/green]\n")
                            else:
                                console.print("API_KEY: [red]Not connected[/red].\n")
                        else:
                            print(strip)

        else:
            label('ERROR',
                  'No .env file found in this directory',
                  Colors.red, True)
        return

    # handle city argument
    if args.city:
        weather_function(args.city)
        return

    # use default city if no args provided
    if DEFAULT_CITY:
        weather_function(DEFAULT_CITY)
        return

    # fallback if no city is available
    label('ERROR',
          'No default city found in .env file. Use -i for interactive mode or provide a city.',
          Colors.red, True)

