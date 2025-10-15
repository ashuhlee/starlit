from rich.console import Console

console = Console()

# show label to left of text
def label(tag: str, text: str, color: str):
    tag = tag.upper()
    console.print(
        f'\n[bold {Colors.white} on {color}] {tag} [/bold {Colors.white} on {color}] {text}')

class Colors:
    # hex codes
    title = '#7571F9'
    purple = '#9598f7'
    pink = '#F785EE'
    red = '#FF5F87'
    orange = '#F0A475'
    white = '#FFFFFF'

# ascii codes
class Style:
    # reset
    end = '\033[0m'

    # text styles
    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    blink = '\033[5m'
    reverse = '\033[7m'
    hidden = '\033[8m'
    strike = '\033[9m'

    # foreground text colors
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

    # bright foreground colors
    bright_black = '\033[90m'
    bright_red = '\033[91m'
    bright_green = '\033[92m'
    bright_yellow = '\033[93m'
    bright_blue = '\033[94m'
    bright_magenta = '\033[95m'
    bright_cyan = '\033[96m'
    bright_white = '\033[97m'

class Misc:
    point = f'{Style.yellow}•{Style.end} '
    user_input = f'{Style.magenta}{Style.bold} {Style.end}'