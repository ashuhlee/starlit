
import os
import shutil
import argparse
from pathlib import Path
from dotenv import load_dotenv

from starlit.ui.styles import label, console, Colors
from starlit.core.weather_function import weather_function
from starlit.modes.interactive import interactive_mode


def get_config_dir() -> Path:
    return Path.home() / ".config" / "starlit"

def get_env_file() -> Path:
    return get_config_dir() / ".env"

config_dir: Path = get_config_dir() # ~/.config/starlit
env_path: Path = get_env_file() # ~/.config/starlit/.env


def open_editor(config_file) -> bool:

    if not config_file.exists():
        label("ERROR",
              "No .env file found to edit. Run [yellow]`starlit --setup`[/yellow] first",
              Colors.red, True)
        return False

    editor = os.getenv("EDITOR")

    if not editor:
        if os.name == "nt":
            editor = "notepad"
        else:
            editor = "nano"

    os.system(f"{editor} {config_file}")
    label("EDIT", "Opened .env file in default editor", Colors.title, True)

    return True

def setup_app(conf_dir, config_file):

    conf_dir.mkdir(parents=True, exist_ok=True)

    if config_file.exists():

        label("ERROR",
              f".env file already exists at `[link=file://{config_file}]{config_file}[/link]`",
              Colors.red, True)

    else:
        # find .env.example in package directory
        import starlit

        package_dir = Path(starlit.__file__).parent
        example_env = package_dir / ".env.example"

        if example_env.exists():
            shutil.copy(example_env, config_file)

            label("DONE",
                  f"Config created at `[link=file://{config_file}]{config_file}[/link]`",
                  Colors.title, True)

            response = input("\nWould you like to edit the config now? (y/n): ").strip().lower()

            if response in ["y", "yes"]:
                open_editor(config_file)
            else:
                console.print("\nYou can edit the config later with [yellow]`starlit --edit`[/yellow]")

        else:
            label("ERROR", ".env.example not found in package", Colors.red, True)

version = "0.1.1"


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
        help="Create a config folder with .env file"
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

    if env_path.exists():
        load_dotenv(env_path)

    class AppConfig:
        api_key = os.getenv("API_KEY")
        default_city = os.getenv("DEFAULT_CITY", "None")

    class Theme:
        primary = os.getenv("COLOR_1", "Default")
        secondary = os.getenv("COLOR_2", "Default")
        label = os.getenv("LABEL_COLOR", "Default")

    class Settings:
        units = os.getenv("UNITS", "Default")
        disable_anim = os.getenv("DISABLE_ANIMATION", "Default")
        show_dt = os.getenv("SHOW_DT", "Default")
        show_ascii = os.getenv("show_ascii", "Default")
        show_msg = os.getenv("show_msg", "Default")
        show_emoji = os.getenv("SHOW_EMOJI", "Default")
        emoji_type = os.getenv("EMOJI_TYPE", "Default")

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
        print(f"starlit version {version}")
        return

    if not env_path.exists():
        label("ERROR",
              "No config found. Run [yellow]`starlit --setup`[/yellow] to get started",
              Colors.red, True)
        return

    # run interactive mode
    if args.interactive:
        interactive_mode()
        return

    # display config settings
    if args.config:
        api_key_length = 32

        if os.path.exists(env_path):

            label(".ENV","[bold]starlit config[/bold]\n", Colors.dark_pink_2, True)

            if not args.show_full:

                print("API Settings")
                console.print(f"  └─ API Key: {"[green]Connected[/green]" if AppConfig.api_key and len(AppConfig.api_key.strip()) == api_key_length 
                else "[red]Not Connected[/red]"}")

                values = {"true": "Yes", "false": "No"}
                anim = {"false": "Enabled", "true": "Disabled"}

                print("\nDisplay Settings")
                print(f"  ├─ Default City: {AppConfig.default_city.capitalize()}")
                print(f"  ├─ Units: {Settings.units.capitalize()}")
                print(f"  ├─ Animations: {anim.get(Settings.disable_anim.lower(), "Yes")}")

                print(f"  ├─ Show Date & Time: {values.get(Settings.show_dt.lower(), "Yes")}")
                print(f"  ├─ Show Ascii: {values.get(Settings.show_ascii.lower(), "Yes")}")
                print(f"  ├─ Show Message: {values.get(Settings.show_msg.lower(), "Yes")}")

                print(f"  ├─ Show Emojis: {values.get(Settings.show_emoji.lower(), "Yes")}")
                print(f"  └─ Emoji Type: {Settings.emoji_type}")

                print("\nColor Settings")

                print(f"  ├─ Color 1: {Theme.primary}")
                print(f"  ├─ Color 2: {Theme.secondary}")
                print(f"  └─ Label Color: {Theme.label}")

                console.print(f"\n[dim white]Config location: [link=file://{env_path}]{env_path}[/link][/dim white]")
                console.print("\nTo show full contents of the .env file, use [yellow]`-c --show-full`[/yellow]")

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

                console.print(f"\n[dim white]Config location: [link=file://{env_path}]{env_path}[/link][/dim white]")

        else:
            label("ERROR", "No .env file found in this directory", Colors.red, True)
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