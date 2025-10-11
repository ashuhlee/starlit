from src.imports import *
from src.main import clear_screen
from src.ui.styles import Style


def load_api_key():
    load_dotenv()

    api_key: str = os.getenv('API_KEY')

    if not api_key:
        print('Error: API Key not found.')
        sys.exit(1)
    else:
        print(Style.yellow + 'API Key found!' + Style.end)
        time.sleep(1)
        clear_screen()

    return api_key