from .core.weather_function import *
from .utils.system_utils import clear_screen, force_quit, exit_app

def interactive_mode():

    clear_screen()
    # interactive mode: runs a loop
    while True:
        label('start', 'Interactive mode', Colors.title, False)

        console.print(f'\n[bold {Colors.title}]Enter city name: [/bold {Colors.title}]')

        city_name: str = input(f'{Misc.user_input}')

        if city_name.lower() in ('q', 'quit'):
            force_quit()

        if weather_function(city_name):
            # city found → ask if user wants to continue
            while True:
                choice = console.input(
                    f'\n[bold {Colors.title}]Explore another forecast?[/bold {Colors.title}] [magenta] [/magenta]').lower()

                if choice.lower() in ('y', 'yes'):
                    clear_screen()
                    break  # start new search

                elif choice.lower() in ('n', 'no'):
                    exit_app()

                elif choice.lower() in ('q', '-q', '--quit', 'quit'):
                    force_quit()

                else:
                    label("warn", "Please enter 'y' or 'n' ", Colors.orange, True)  # prompt again
        else:
            # city not found → ask again (outer loop continues)
            continue
