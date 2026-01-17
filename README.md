
<div align="center">

# starlit
A minimal and customizable weather CLI, written in Python 🐍

![preview](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/cover.png)
Powered by the OpenWeatherMap API and styled with the Python rich library + terminal text effects ✨


[![GitHub Repo stars](https://img.shields.io/github/stars/ashuhlee/starlit?style=for-the-badge&logo=starship&logoColor=%23D7E0ED&labelColor=%232F2D42&color=%23FFBDF2)](https://github.com/ashuhlee/starlit/stargazers)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/ashuhlee/starlit?style=for-the-badge&logo=gitbook&logoColor=%23D9E0EE&labelColor=%232F2D42&color=FFD0CF)](https://github.com/ashuhlee/starlit/issues)
[![GitHub Release](https://img.shields.io/github/v/release/ashuhlee/starlit?style=for-the-badge&logo=github&logoColor=%23D9E0EE&labelColor=%232F2D42&color=BBC0FF&label=version)](https://github.com/ashuhlee/starlit/releases)
[![GitHub repo size](https://img.shields.io/github/repo-size/ashuhlee/starlit?style=for-the-badge&logo=removedotbg&logoColor=%23D9E0EE&labelColor=%232F2D42&color=AEE5FF)](https://github.com/ashuhlee/starlit)


</div>

## Requirements
- Python 3.13+
- Poetry or pip package manager
- An [OpenWeatherMap](https://openweathermap.org) API key
- UTF-8 terminal with 256 colors and nerd font

<p align="center">
  <img
    src="https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-7.png"
    alt="preview"
    width="700"
  >
</p>


## Installation
Installing starlit is quick and easy. The built-in setup command guides you through configuration.

### Option 1: Install with pipx

The easiest way to install starlit is via pipx:
```zsh
pipx install starlit-cli
```

Then set up your configuration:
```zsh
starlit --setup # creates ~/.config/starlit/.env
starlit --edit  # opens .env file (add your api key here) 
```

To upgrade to the latest version:
```zsh
pipx upgrade starlit-cli
```

### Option 2: Install from source

For local development or contributing:

1. **Clone this repository**
```zsh
git clone https://github.com/ashuhlee/starlit.git
cd starlit
```
2. **Create the virtual environment**
```zsh
# macOS / Linux / Windows
python -m venv .venv
```

Activate the virtual environment:
```zsh
source .venv/bin/activate # macOS / Linux
.venv\Scripts\Activate    # Windows (Powershell)
```

3. **Install in editable mode**

Some packages are required for this project. They will automatically be installed if you run:
```zsh
pip install -e .
```
4. **Set up your configuration**

Generates a configuration file from the example template and open the file:

```zsh
starlit --setup
starlit --edit
```

To update your installation:
```zsh
git pull origin main
pip install -e .
```

Get your [OpenWeatherMap API key](https://openweathermap.org/api) and paste it into the `.env` file under `API_KEY=`

## Configuration
`starlit` creates a default configuration file when you run `starlit --setup`. The `.env` file stores your API key, default city and display preferences.

- Linux/macOS: `~/.config/starlit/.env`
- Windows: `C:\users\username\.config\starlit\.env`


| Setting             | Description                               |
|---------------------|-------------------------------------------|
| `API_KEY`           | Your OpenWeatherMap API key               |
| `DEFAULT_CITY`      | The city shown when you don’t pass one    |
| `UNITS`             | Options: `metric` (°C) or `imperial` (°F) |
| `DISABLE_ANIMATION` | Turns off all animations in starlit       |
| `SHOW_DT`           | Shows local date and time                 |
| `SHOW_ASCII`        | Shows the little ASCII art to the left    |
| `SHOW_MSG`          | Adds a cute message at the bottom         |
| `SHOW_EMOJI`        | Shows emojis in your terminal             |
| `EMOJI_TYPE`        | Choose a cute emoji for messages          |


### Customize colors
You can also set your own colors for the gradient title and message labels.
Use **six-digit** RGB hex codes (no # needed):

| Setting     | Description           | Example                                                                                                                        |
|-------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|
| COLOR_1     | Gradient color stop 1 | <img src="https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/colors/1.png" alt="color1" width="10"/> 5D63FF |
| COLOR_2     | Gradient color stop 2 | <img src="https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/colors/2.png" alt="color1" width="10"/> F7A4F4 |
| LABEL_COLOR | Message label color   | <img src="https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/colors/3.png" alt="color1" width="10"/> 5CE7F9 |

## Usage

```zsh
# basic usage
starlit

# specify city via command line
starlit seattle

# start interactive mode
starlit --interactive 

# opens the .env file in your default editor
starlit --edit

# shows config in .env file (if found)
starlit --config

# shows contents of .env file (if found)
starlit --config --show-full

# show version
starlit --version

# show help
starlit --help
```

## Usage examples

| ![preview-1](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-1.png) | ![preview-2](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-2.png) |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![preview-3](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-3.png) | ![preview-4](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-4.png) |
| ![preview-5](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-5.png) | ![preview-6](https://raw.githubusercontent.com/ashuhlee/starlit/main/assets/images/previews/preview-6.png) |


## What's next
- **Different Modes:** Add live updates or full forecast modes
- **Interactive Mode+:** Add a full command line interface when using `starlit -i`
- **Color Themes:** Support for `.json` theme files so you can easily switch between color palettes
- **Multi-language Support:** Option to view weather info in different languages

## Tech stack

- **[Rich](https://github.com/Textualize/rich)** - Beautiful terminal formatting
- **[rich-gradient](https://github.com/maxludden/rich-gradient)** - Gradient text formatting
- **[terminal-text-effects](https://github.com/ChrisBuilds/terminaltexteffects)** - Smooth text animations
- **[Requests](https://pypi.org/project/requests/)** - HTTP requests for weather API
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management


## About this project
I built this fun little project as a way to learn more about APIs and creating colorful terminal apps. It grew into a CLI project I'm proud of!

Thank you to [charm](https://github.com/charmbracelet) for the color palette and design interface inspo 🎨 and to [wego](https://github.com/schachmat/wego/tree/master) for the ASCII icons

⭐ If you like this project, please consider giving it a star!