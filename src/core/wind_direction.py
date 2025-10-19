def wind_arrow(deg: float) -> str:
    if deg >= 337.5 or deg < 22.5:
        return '↑'
    elif 22.5 <= deg < 67.5:
        return '↗'
    elif 67.5 <= deg < 112.5:
        return '→'
    elif 112.5 <= deg < 157.5:
        return '↘'
    elif 157.5 <= deg < 202.5:
        return '↓'
    elif 202.5 <= deg < 247.5:
        return '↙'
    elif 247.5 <= deg < 292.5:
        return '←'
    elif 292.5 <= deg < 337.5:
        return '↖'
    else:
        return ''