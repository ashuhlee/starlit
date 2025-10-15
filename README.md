# weather-cli 🌥️
weather-cli is a lightweight and colorful terminal application that lets you check the current weather for any city in the world.

Powered by the OpenWeatherMap API and styled with the Python rich library + terminal text effects ✨

![preview](preview/preview-1.gif)

## Requirements
- Python 3.13+
- pip package manager
- An [OpenWeatherMap](https://openweathermap.org) API key

## Installation
1. **Clone this repository**
```zsh
git clone https://github.com/ashuhlee/weather-cli.git
cd weather-cli
```
2. **Install dependencies**

Some packages are required for this project. They will automatically be installed if you run:
```zsh
pip install -e .
```
3. **Create a `.env` file to store your API key.**
```
echo "API_KEY=your_openweather_api_key" > api.env
```
> Get your API key from [OpenWeatherMap](https://openweathermap.org/api)

## Usage
Simply run this command and follow the interactive prompts:

```zsh
weather-cli
```

## Example session
![preview](preview/preview-2.png)

## Project structure
```
weather-cli/
├── src/                      # Main source code folder
│   ├── main.py               # Entry point of the CLI app
│   │
│   ├── core/                
│   │   ├── __init__.py       # Makes `core` a Python package
│   │   └── timezone.py       # Handles fetching timezone
│   │
│   └── ui/                   # User interface components and styling
│       ├── __init__.py       # Makes `ui` a Python package
│       ├── animations.py     # Text and terminal animations
│       ├── emojis.py         # Emoji definitions
│       ├── styles.py         # Colors, ascii codes, and formatting
│       └── system_utils.py   # System-level actions (exit, clear screen, etc.)
│
├── .env                      # Stores OpenWeatherMap API key
├── .gitignore               
├── README.md                
└── setup.py                  # Configuration for packaging & installing the CLI

```

## What's next?
**Help Menu:** Add a help guide for new users using flags
```zsh
weather-cli -h
```
```zsh
weather-cli --help
```
**Direct Arguments:** Ability to pass city names directly from the terminal, for example:
```zsh
weather-cli seattle
```

## Tech stack

- **[Rich](https://github.com/Textualize/rich)** - Beautiful terminal formatting
- **[terminal-text-effects](https://github.com/ChrisBuilds/terminaltexteffects)** - Smooth text animations
- **[Requests](https://pypi.org/project/requests/)** - HTTP requests for weather API
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management
---
### About this project
I built this fun little project as a way to learn more about APIs and creating colorful terminal apps. It turned into a CLI project I'm proud of!

This project is an active work in progress. Thank you to [charm](https://github.com/charmbracelet) for the color palette inspo 🎨

⭐ If you found this project helpful, please consider giving it a star!