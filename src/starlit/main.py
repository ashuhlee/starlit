
import os
import argparse
import sys
from pathlib import Path
from typing import override
from dotenv import load_dotenv

from starlit.config.onboarding import onboarding_prompt
from starlit.config.settings import show_config
from starlit.config.setup import get_config_dir, get_env_file, open_editor, setup_app
from starlit.config.show_help import show_help

from starlit.ui.styles import label, console, Colors
from starlit.core.interactive import interactive_mode
from starlit.core.weather_function import weather_function

from starlit import __version__


config_dir: Path = get_config_dir() # ~/.config/starlit
env_path: Path = get_env_file() # ~/.config/starlit/.env


class CustomArgParser(argparse.ArgumentParser):
    @override
    def error(self, message: str):

        flg: str = Colors.light_pink

        if "unrecognized arguments:" in message:
            flag = message.split("unrecognized arguments:")[1].strip()
            label("ERROR", f"Unknown flag: {flag}\n\nTry [{flg}]--help[/{flg}] for usage", Colors.red, True)
        else:
            label("ERROR", message, Colors.red, True)

        sys.exit(2)


def main():

    parser = CustomArgParser(prog="starlit", add_help=False)

    parser.add_argument("city", nargs="*",
        help="City name to fetch weather for")

    parser.add_argument("-h", "--help",
        action="store_true", help="Show help")

    parser.add_argument("-s", "--setup",
        action="store_true", help="Create a config folder with .env file")

    parser.add_argument("-i", "--interactive",
        action="store_true", help="Start interactive mode")

    parser.add_argument("-v", "--version",
        action="store_true", help="Show the version")

    parser.add_argument("-c", "--config",
        action="store_true", help="View config settings in the terminal")

    parser.add_argument("--show-full",
        action="store_true", help="Show full config file contents")

    parser.add_argument("-e", "--edit",
        action="store_true", help="Open config file for editing")

    args = parser.parse_args()

    if env_path.exists():
        load_dotenv(env_path)

    default_city = os.getenv("DEFAULT_CITY")

    if args.help:
        show_help()
        return

    # copies .env.example to ~/.config/starlit/.env
    if args.setup:
        setup_app(config_dir, env_path)
        return

    # open config file in default editor
    if args.edit:
        open_editor(env_path)
        return

    # print version
    if args.version:
        label(f"v{__version__}","[bold]starlit version[/bold]", Colors.dark_pink_2, True)
        return

    if not env_path.exists():
        onboarding_prompt()
        return

    # run interactive mode
    if args.interactive:
        interactive_mode()
        return

    # display config settings
    if args.config:

        label(".ENV", "[bold]starlit config[/bold]\n", Colors.dark_pink_2, True)
        show_config(env_path, args.show_full)

        console.print(f"\n[dim white]Config location: [link=file://{env_path}]{env_path}[/link][/dim white]")
        return

    # handle city argument
    if args.city:
        city_name = " ".join(args.city)
        weather_function(city_name)
        return

    # use default city if no args provided
    if default_city:
        weather_function(default_city)
        return

    # fallback if no city is available
    label("ERROR",
          "No default city found in .env file. Use -i for interactive mode or provide a city.",
          Colors.red, True)



if __name__ == "__main__":
    main()