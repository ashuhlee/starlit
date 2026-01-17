import os
import sys
import shutil
import getpass
from pathlib import Path

from starlit.ui.animations import spinner
from starlit.ui.styles import label, Colors, console


def get_config_dir() -> Path:
    return Path.home() / ".config" / "starlit"


def get_env_file() -> Path:
    return get_config_dir() / ".env"


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
                  f"Config created at [{Colors.light_pink}]`[link=file://{config_file}]{config_file}[/link]`[/{Colors.light_pink}]",
                  Colors.title, True)
            try:

                # manual setup
                if not start_guide("  Start guided setup? (y/n): "):
                    console.print("\n  [b]Ok.[/b] You can edit the config later with [yellow]`starlit --edit`[/yellow]")
                    return

                onboarding()

            except KeyboardInterrupt:
                print()
                label("EXIT", "Setup interrupted. Progress has been saved!", Colors.title, True)

        else:
            label("ERROR", ".env.example not found in package", Colors.red, True)


def start_guide(prompt: str) -> bool:

    while True:
        response = input(f"\n{prompt}").strip().lower()

        if response in ["y", "yes"]:
            return True
        elif response in ["no", "n"]:
            return False

def onboarding():

    set_api_key()
    set_default_city()
    set_unit()

    console.print("\n  [b]Setup complete![/b] 💫 🌟 ✨")
    console.print("   - Run [yellow]`starlit --edit`[/yellow] to make further changes later.")


def update_config(config_file: Path, key: str, value: str):

    lines = config_file.read_text().splitlines()
    updated_lines = []

    for line in lines:
        if line.startswith(f"{key}="):
            updated_lines.append(f"{key}={value}")
        else:
            updated_lines.append(line)

    config_file.write_text("\n".join(updated_lines) + "\n")


def set_api_key():

    console.print("\n  Starlit requires an OpenWeather API key to display weather data.")
    check_key = input("  Do you have an OpenWeather API key? (y/n): ").strip().lower()

    while check_key not in ["y", "yes", "n", "no"]:
        check_key = input("\n  Do you have an OpenWeather API key? (y/n): ").strip().lower()

    if check_key in ["y", "yes"]:
        SET_KEY = getpass.getpass("\n  Enter your API key ").strip()

        if not (SET_KEY and len(SET_KEY.strip()) == 32):
            label("UH OH", "Invalid API key. Starlit can't run without it! \nYou can set your API key later with [yellow]`starlit --edit`[/yellow]",
                  Colors.red, True)

        else:
            update_config(get_env_file(), "API_KEY", SET_KEY)
            label("DONE", "API key validated!", Colors.title, True)

    elif check_key in ["no", "n"]:
        console.print("\n  You can set your API key later with [yellow]`starlit --edit`[/yellow]. Starlit can't run without it!")


def set_default_city():

    default_city = input("\n  Set your default city: ").title()

    if default_city:
        update_config(get_env_file(), "DEFAULT_CITY", default_city)
        label("DONE", f"Default city set to {default_city}", Colors.title, True)
    else:
        console.print("  No default city set. You can add one later.")


def set_unit():
    while True:
        default_unit = input("\n  Set unit system ([M]etric / [I]mperial): ").strip().lower()

        if default_unit in ["m", "metric", ""]:
            default_unit = "metric"
            label("DONE", f"Unit system set to {default_unit}", Colors.title, True)
            break

        elif default_unit in ["i", "imperial"]:
            default_unit = "imperial"
            label("DONE", f"Unit system set to {default_unit}", Colors.title, True)
            break

        else:
            label("UH OH", "Invalid unit. Default set to metric", Colors.red, True)
            default_unit = "metric"
            break

    update_config(get_env_file(), "UNITS", default_unit)
