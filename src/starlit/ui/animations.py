
from starlit.utils.system_utils import *

from terminaltexteffects import Color
from terminaltexteffects.effects.effect_print import Print


# gradient text animation
def text_effect(text: str, speed: int, colors: tuple = (color1_tte, color2_tte)) -> None:

    effect = Print(text)

    effect.effect_config.print_speed = speed
    effect.effect_config.final_gradient_stops = tuple(Color(c) for c in colors)

    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


# spinning animation for loading data
def spinner(text: str, duration: float, found: bool | None, display: bool = True) -> None:

    if display:
        print()

        with console.status(f'[cyan]{text}[/cyan]', spinner='dots', spinner_style='magenta'):
            time.sleep(duration) # length of animation

        if found:
            print(hide_cur, end='', flush=True)
            console.print('[green]󰄬 Data fetched successfully![/green]')

            sys.stdout.write('\x1b[1A')  # move cursor up
            time.sleep(0.25)

            sys.stdout.write('\x1b[2K')  # clears line
        else:
            pass
