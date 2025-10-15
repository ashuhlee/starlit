
from ui.system_utils import *

from ui.styles import Style, Colors, label

from terminaltexteffects import Color
from terminaltexteffects.effects.effect_print import Print

# gradient text animation
def text_effect(text: str, speed: int, colors: tuple = ('7571F9', 'f7a4f4')):

    effect = Print(text)

    effect.effect_config.print_speed = speed
    effect.effect_config.final_gradient_stops = tuple(Color(c) for c in colors)

    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

# spinning animation for loading data
def spinner(text: str, duration: float, found: bool | None) -> None:

    print()
    with console.status(f'[cyan]{text}[/cyan]', spinner='dots', spinner_style='magenta'):
        # length of animation
        time.sleep(duration)

    if found:
        console.print('[green]󰄬 Data fetched successfully![/green]')
    else:
        pass

# typewriter effect for text
def typewriter(text: str, speed: float, delay: float, cursor: bool) -> None:
    if not cursor:
        # hide terminal cursor
        print(hide_cur, end='', flush=True)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

    print()

    time.sleep(delay)

# animated plane
def plane_anim():
    plane: str = '✈️'

    path_length: int = 18
    anim_length: int = 4
    static_length: int = path_length - anim_length  # dashes except the last 5

    bold_dash: str = f'{Style.bold}-{Style.end}'

    print(hide_cur, end='', flush=True)

    for i in range(anim_length):  # animate last 5 dashes
        # static dashes
        static_line = f'{Style.bold}- {Style.end}' * static_length

        # animated dashes
        anim_line = (bold_dash + ' ') * i
        spaces = ' ' * (2 * (anim_length - i))

        # concat all the lines
        line = static_line + anim_line + plane + spaces

        sys.stdout.write('\r' + line)
        sys.stdout.flush()
        time.sleep(0.08)

    print(show_cur)