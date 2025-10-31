
from rich.console import Console
from rich.rule import Rule

from starlit.ui.styles import label, Colors
from starlit.ui.helpers import *

hide_cur = '\033[?25l'
show_cur = '\033[?25h'

console = Console()

warnings_log = []

def log_warning(msg: str):
    warnings_log.append(msg)


def print_warnings():

    if len(warnings_log) == 1:
        rule = Rule('1 config error', characters='-', style='grey', align='left')
        console.print('', rule, width=50)

    elif len(warnings_log) == 0:
        pass
    else:
        rule = Rule(f'{len(warnings_log)} config errors', characters='-', style='grey', align='left')
        console.print('', rule, width=50)

    for w in warnings_log:
        label('warn', w, Colors.orange, True)


# check if label custom color is valid
if not is_valid_hex(Colors.CUSTOM_LABEL):

    error = f"Invalid LABEL_COLOR. Using default [#{Colors.dark_pink}]#{Colors.dark_pink}[/#{Colors.dark_pink}]"
    log_warning(error)

    Colors.custom_label  = f'#{Colors.dark_pink}'

# check if color 1 is valid (terminal text effects)
if not is_valid_hex(color1_tte):

    error = f"Invalid COLOR_1. Using default [#{Colors.DEFAULT_1}]#{Colors.DEFAULT_1}[/#{Colors.DEFAULT_1}]"
    log_warning(error)

    color1_tte = DEFAULT_1_TTE

# check if color 2 is valid (terminal text effects)
if not is_valid_hex(color2_tte):

    error = f"Invalid COLOR_2. Using default [#{Colors.DEFAULT_2}]#{Colors.DEFAULT_2}[/#{Colors.DEFAULT_2}]"
    log_warning(error)

    color2_tte = DEFAULT_2_TTE

# exit app
def exit_app():

    print(hide_cur)
    clear_screen()
    label('exit', 'Exited interactive mode', Colors.title, False)

    print(show_cur, end='', flush=True)
    sys.exit(0)

# force quit app
def force_quit():

    label('exit', 'Force quitting starlit', Colors.orange, True)
    sys.exit(0)

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')