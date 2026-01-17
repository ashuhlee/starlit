from rich.console import Console
from rich_gradient import Text

from starlit.ui.helpers import *

console = Console()

class Colors:

    DEFAULT_1 = '7571F9'
    DEFAULT_2 = 'F7A4F4'

    # hex codes
    title = '#7571F9'
    purple = '#9598f7'
    aqua = '#7AD4F5'
    pink = '#F785EE'

    light_pink = '#F7A1FF'

    dark_pink = 'F06EE6'
    dark_pink_2 = '#F06EE6'

    red = '#FF448A'
    orange = '#F09564'
    green = '#32A852'
    white = '#FFFFFF'

    CUSTOM_LABEL = os.getenv('LABEL_COLOR', dark_pink)  # defaults to dark pink
    custom_label = f'#{CUSTOM_LABEL}'


# show label to left of text
def label(tag: str, text: str, color: str, newline: bool, sys_exit: bool = True):
    tag = tag.upper()

    console.print(f'{'\n' if newline else ''}[bold {Colors.white} on {color}] {tag} [/bold {Colors.white} on {color}] {text}')

    if tag == 'ERROR' and sys_exit:
        sys.exit(1)

def gradient_text(text: str):

    color1 = make_valid_hex(color1_rich, DEFAULT_1_RICH)
    color2 = make_valid_hex(color2_rich, DEFAULT_2_RICH)

    print()
    console.print(Text(text.rstrip('\n'), colors=[color1, color2]))
    print('\033[?25h', end = '') # show cursor

# ascii codes
class Style:
    end = '\033[0m'
    bold = '\033[1m'
    yellow = '\033[33m'
    magenta = '\033[35m'

class Misc:
    divider = f'{Style.yellow}›{Style.end} '
    user_input = f'{Style.magenta}{Style.bold} {Style.end}'