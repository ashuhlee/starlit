
from rich.rule import Rule
from rich.text import Text

from starlit.core.weather_function import *
from starlit.utils.system_utils import console, clear_screen, exit_app


def show_header(city: str = ''):
    header_text = Text()

    local_time = datetime.now().strftime('%b %d, %I:%M %p')

    if city:
        header_text.append(city, style='dim magenta')
        header_text.append('  •  ', style='dim white')

    header_text.append(local_time + '  •  ', style='dim white')
    header_text.append('press ctrl+c to quit', style='dim white')

    rule = Rule(title=header_text, style='dim white', align='right')
    console.print(rule)
    print()

    label('start', 'Interactive mode', Colors.title, False)


def interactive_mode():

    try:
        clear_screen()
        show_header()

        while True:
            # interactive mode: runs a loop
            console.print(f'\n[bold {Colors.title}]Enter city name: [/bold {Colors.title}]')
            city_name: str = input(f'{Misc.user_input}').strip().lower()
            city_name = ' '.join(city_name.split())

            if city_name in ('q', 'quit', '--quit'):
                raise KeyboardInterrupt

            clear_screen()
            show_header(city_name.capitalize())

            if weather_function(city_name):
                # city found → ask if user wants to continue
                while True:
                    choice = console.input(
                        f'\n[bold {Colors.title}]Explore another forecast?[/bold {Colors.title}] [magenta] [/magenta]').lower()

                    if choice.lower() in ('y', 'yes'):
                        clear_screen()
                        show_header()
                        break  # start new search

                    elif choice.lower() in ('n', 'no', 'q', 'quit', '--quit'):
                        raise KeyboardInterrupt

                    else:
                        label("warn", "Please enter 'y' or 'n' ", Colors.orange, True)  # prompt again
            else:
                # city not found → ask again (outer loop continues)
                continue

    except KeyboardInterrupt:
        console.print("\n[dim white]Exiting interactive mode...[/dim white]")
        exit_app()
