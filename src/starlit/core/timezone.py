from datetime import datetime, timezone, timedelta
from starlit.ui.styles import Misc


def get_local_time(offset_seconds: int, return_dt: bool = False):

    utc_dt: datetime = datetime.now(timezone.utc)

    local_time: datetime = utc_dt + timedelta(seconds=offset_seconds)
    offset_hours: int = offset_seconds // 3600

    if offset_hours >= 0:
        gmt_label: str = 'GMT+'.lower() + str(offset_hours)
    else:
        gmt_label: str = 'GMT'.lower() + str(offset_hours)

    formatted_time: str = local_time.strftime('%I:%M %p')

    if return_dt:
        return utc_dt, local_time

    return f'{formatted_time} ({gmt_label})'


def get_local_date(offset_seconds: int) -> str:

    utc_dt: datetime = datetime.now(timezone.utc)

    local_time = utc_dt + timedelta(seconds=offset_seconds)

    # format: Thu. Oct 16
    return local_time.strftime(f'%a. %b {local_time.day}')

def get_sun_time(sunrise_arg: int, sunset_arg: int, offset_seconds: int) -> str:

    local_time, utc_dt = get_local_time(offset_seconds, return_dt = True)

    sunrise_local = datetime.fromtimestamp(sunrise_arg, timezone.utc) + timedelta(seconds=offset_seconds)
    sunset_local = datetime.fromtimestamp(sunset_arg, timezone.utc) + timedelta(seconds=offset_seconds)

    if local_time < sunrise_local:
        # show todays sunrise
        return f'sunrise  {Misc.divider}  {sunrise_local.strftime('%I:%M %p')}'

    elif local_time < sunset_local:
        # show todays sunset (between sunrise and sunset)
        return f'sunset   {Misc.divider}  {sunset_local.strftime('%I:%M %p')}'

    else:
        # sunset the next day if past sunrise
        return f'sunrise  {Misc.divider}  {(sunrise_local + timedelta(days = 1)).strftime('%I:%M %p')}'
