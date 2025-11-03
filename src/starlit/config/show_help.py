
from rich.padding import Padding
from starlit.ui.styles import console, Colors


# a prettier help menu
def show_help():

    console.print("\nStarlit is a minimal, cute and customizable weather cli.",
                  "\nWeather forecasts, beautifully styled for your terminal!")

    # usage section
    usage = f"[yellow]starlit[/yellow] [not b dim]\\[city] [--flags][/not b dim]{' ':11}"

    console.print(f"\n[bold {Colors.title}]USAGE[/bold {Colors.title}]\n")
    console.print(Padding(usage, (1,2), style="on #2a2a34", expand=False))

    # example section
    console.print(f"\n[bold {Colors.title}]EXAMPLES[/bold {Colors.title}]\n")

    examples = [
        ("# Get weather for default city", "starlit", ""),
        ("# Get weather for a specific city", "starlit", "tokyo"),
        ("# Start interactive mode", "starlit", "--interactive")
    ]

    lines = []
    for comment, name, cmd in examples:
        lines.append(f"[dim]{comment}[/dim]")
        lines.append(f"[yellow]{name}[/yellow] {cmd}")
        lines.append("")

    examples_str = "\n".join(lines[:-1])

    console.print(Padding(examples_str, (1, 3), style="on #2a2a34", expand=False))

    # flags section
    console.print(f"\n[bold {Colors.title}]FLAGS[/bold {Colors.title}]\n")

    commands = [
        ("-s --setup", "Create configuration folder with .env file"),
        ("-e --edit", "Open configuration file in default editor"),
        ("-c --config", "View configuration settings in terminal"),
        ("-i --interactive", "Start interactive mode"),
        ("-v --version", "Show starlit version"),
        ("-h --help", "Show this help message"),
    ]

    for cmd, desc in commands:
        console.print(f"  [{Colors.light_pink}]{cmd:25}[/{Colors.light_pink}] {desc}")

    console.print()
