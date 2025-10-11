from src.imports import *

def typewriter(text: str, speed: float):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)