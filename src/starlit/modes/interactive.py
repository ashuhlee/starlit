from starlit.core.weather_function import *
from starlit.utils.system_utils import console, clear_screen, force_quit, exit_app

def interactive_mode():

    clear_screen()
    label('start', 'Interactive mode', Colors.title, False)

    while True:
        # interactive mode: runs a loop
        console.print(f'\n[bold {Colors.title}]Enter city name: [/bold {Colors.title}]')

        city_name: str = input(f'{Misc.user_input}')

        if weather_function(city_name):
            # city found → ask if user wants to continue
            while True:
                choice = console.input(
                    f'\n[bold {Colors.title}]Explore another forecast?[/bold {Colors.title}] [magenta] [/magenta]').lower()

                if choice.lower() in ('y', 'yes'):
                    clear_screen()
                    label('start', 'Interactive mode', Colors.title, False)
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
