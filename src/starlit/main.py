
import os
import shutil
import argparse
from starlit.ui.styles import label, Colors, Console, load_dotenv
from starlit.core.weather_function import weather_function
from starlit.interactive_mode import interactive_mode

load_dotenv()
console = Console()

class AppConfig:
    api_key = os.getenv('API_KEY')
    default_city = os.getenv("DEFAULT_CITY", None)

class Theme:
    primary = os.getenv('COLOR_1', 'Default')
    secondary = os.getenv('COLOR_2', 'Default')
    label = os.getenv('LABEL_COLOR', 'Default')

class Settings:
    units = os.getenv('UNITS', 'Default')
    disable_anim = os.getenv('DISABLE_ANIMATION', 'Default')
    show_dt = os.getenv('SHOW_DT', 'Default')
    show_ascii = os.getenv('show_ascii', 'Default')
    show_msg = os.getenv('show_msg', 'Default')
    show_emoji = os.getenv('SHOW_EMOJI', 'Default')
    emoji_type = os.getenv('EMOJI_TYPE', 'Default')

version = "0.1.0"

def main():
    parser = argparse.ArgumentParser(
        prog="starlit",
        description="A minimal, cute and customizable weather cli. ☁️",
    )

    # optional pos argument for city (default if none)
    parser.add_argument("city", nargs="*",
        help="City name to fetch weather for"
    )

    # copy .env.example to new .env file
    parser.add_argument("--setup",
        action="store_true",
        help="Create a .env file from .env.example"
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

    # copies .env.example to new .env file
    if args.setup:

        example_path = os.path.join(os.getcwd(), ".env.example")
        target_path = os.path.join(os.getcwd(), ".env")

        if os.path.exists(target_path):
            label('ERROR','.env file already exists', Colors.red, True)

        elif os.path.exists(example_path):
            shutil.copy(example_path, target_path)
            label('SUCCESS', 'Copied .env.example to .env successfully!', Colors.green, True)

        else:
            label('ERROR','.env.example file not found in package directory', Colors.red, True)

        return


    # open config file in default editor
    if args.edit:
        env_path = ".env"

        if os.path.exists(env_path):
            editor = os.getenv("EDITOR")

            if not editor:
                # windows operating system
                if os.name == "nt":
                    editor = "notepad"
                # unix operating system
                else:
                    editor = "nano"

            os.system(f"{editor} {env_path}")
        else:
            label('ERROR', 'No .env file found to edit', Colors.red, True)
        return

    # print version
    if args.version:
        print(f"starlit version {version}")
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
                console.print(f"  └─ API Key: {"[green]Connected[/green]" if AppConfig.api_key and len(AppConfig.api_key.strip()) == api_key_length 
                else '[red]Not Connected[/red]'}")

                values = {"true": "Yes", "false": "No"}
                anim = {"false": "Enabled", "true": "Disables"}

                print("\nDisplay Settings:")
                print(f"  ├─ Default City: {AppConfig.default_city.capitalize()}")
                print(f"  ├─ Units: {Settings.units.capitalize()}")
                print(f"  ├─ Animations: {anim.get(Settings.disable_anim.lower(), "Yes")}")

                print(f"  ├─ Show Date & Time: {values.get(Settings.show_dt.lower(), "Yes")}")
                print(f"  ├─ Show Ascii: {values.get(Settings.show_ascii.lower(), "Yes")}")
                print(f"  ├─ Show Message: {values.get(Settings.show_msg.lower(), "Yes")}")

                print(f"  ├─ Show Emojis: {values.get(Settings.show_emoji.lower(), "Yes")}")
                print(f"  └─ Emoji Type: {Settings.emoji_type}")

                print("\nColor Settings:")

                print(f"  ├─ Color 1: {Theme.primary}")
                print(f"  ├─ Color 2: {Theme.secondary}")
                print(f"  └─ Label Color: {Theme.label}")

                console.print("\nTo show full contents of the .env file, append the flag [yellow]--show-full[/yellow]")

            else:

                with open(env_path, "r", encoding="utf-8") as f:

                    for line in f:
                        strip = line.strip()

                        # hide api key in terminal
                        if strip.startswith("API_KEY="):
                            if AppConfig.api_key and len(AppConfig.api_key.strip()) == api_key_length:
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
        city_name = " ".join(args.city)
        weather_function(city_name)
        return

    # use default city if no args provided
    if AppConfig.default_city:
        weather_function(AppConfig.default_city)
        return

    # fallback if no city is available
    label('ERROR',
          'No default city found in .env file. Use -i for interactive mode or provide a city.',
          Colors.red, True)


if __name__ == "__main__":
    main()