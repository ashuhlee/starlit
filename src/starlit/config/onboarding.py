
from rich.console import Console
from rich.style import Style
from rich.text import Text
from rich.table import Table

console = Console()

def onboarding_prompt():
    title = "Starlit"
    steps = 5

    table = Table(show_header=False, show_edge=False, box=None, padding=(0, 2))

    left_text = Text()
    right_text = Text()

    rule = "─" * 60

    # pastel gradient color palette
    colors = ["#F06EE6", "#d76fea", "#b96fef", "#9470f4", "#7571F9"]

    for i in range(steps):
        bg = colors[i]
        style = Style(bgcolor=bg, color="#f7e9b0", italic=True)

        space = "  " * i
        line = Text(space)
        line.append(f" {title} ", style=style)

        if i < (steps - 1):
            line.append("\n")

        left_text.append(line)

    right_text.append("\nA minimal and customizable weather cli, written in Python 🌦️\n")
    right_text.append(rule + "\n", style="dim grey35")
    right_text.append_text(Text.from_markup("Run [yellow]`starlit --setup`[/yellow] to setup a config file"))

    table.add_row(left_text, right_text)
    console.print("", table)