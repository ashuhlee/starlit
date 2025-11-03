import os
import shutil
from pathlib import Path

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
                  f"Config created at `[link=file://{config_file}]{config_file}[/link]`",
                  Colors.title, True)

            response = input("\nWould you like to edit the config now? (y/n): ").strip().lower()

            while (response not in ["y", "yes", "n", "no"]):
                    response = input("\nWould you like to edit the config now? (y/n): ").strip().lower()
            if response in ["y", "yes"]:
                open_editor(config_file)
            elif response in ["no", "n"]:
                console.print("\nYou can edit the config later with [yellow]`starlit --edit`[/yellow]")
                

        else:
            label("ERROR", ".env.example not found in package", Colors.red, True)
