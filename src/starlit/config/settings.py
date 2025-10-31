import os
from starlit.ui.styles import console, Colors


def show_config(env_file, show_full: bool):

    api_key = os.getenv("API_KEY", "")
    default_city = os.getenv("DEFAULT_CITY", "None")

    api_key_length = 32

    if not show_full:

        console.print(f"\n[bold {Colors.title}]API SETTINGS[/bold {Colors.title}]\n")

        api_status = "[green]Connected[/green]" if api_key and len(api_key.strip()) == api_key_length else "[red]Not Connected[/red]"
        console.print(f"  └─ API Key: {api_status}")

        values = {"true": "Yes", "false": "No"}
        anim = {"false": "Enabled", "true": "Disabled"}

        console.print(f"\n[bold {Colors.title}]DISPLAY SETTINGS[/bold {Colors.title}]\n")

        print(f"  ├─ Default City: {default_city.capitalize()}")
        print(f"  ├─ Units: {os.getenv('UNITS', 'metric').capitalize()}")
        print(f"  ├─ Animations: {anim.get(os.getenv('DISABLE_ANIMATION', 'false').lower(), 'Enabled')}")
        print(f"  ├─ Show Date & Time: {values.get(os.getenv('SHOW_DT', 'true').lower(), 'Yes')}")
        print(f"  ├─ Show Ascii: {values.get(os.getenv('show_ascii', 'true').lower(), 'Yes')}")
        print(f"  ├─ Show Message: {values.get(os.getenv('show_msg', 'true').lower(), 'Yes')}")
        print(f"  ├─ Show Emojis: {values.get(os.getenv('SHOW_EMOJI', 'true').lower(), 'Yes')}")
        print(f"  └─ Emoji Type: {os.getenv('EMOJI_TYPE', 'default')}")

        console.print(f"\n[bold {Colors.title}]COLOR SETTINGS[/bold {Colors.title}]\n")

        print(f"  ├─ Color 1: {os.getenv('COLOR_1', 'Default')}")
        print(f"  ├─ Color 2: {os.getenv('COLOR_2', 'Default')}")
        print(f"  └─ Label Color: {os.getenv('LABEL_COLOR', 'Default')}")

        console.print("\nTo show full contents, use [yellow]`-c --show-full`[/yellow]")

    else:

        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())