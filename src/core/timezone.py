from datetime import datetime, timezone, timedelta

def get_local_time(offset_seconds: int) -> str:
    utc_dt: datetime = datetime.now(timezone.utc)

    local_time: datetime = utc_dt + timedelta(seconds=offset_seconds)
    offset_hours: int = offset_seconds // 3600

    if offset_hours >= 0:
        gmt_label: str = 'GMT+' + str(offset_hours)
    else:
        gmt_label: str = 'GMT' + str(offset_hours)

    formatted_time: str = local_time.strftime('%I:%M %p')

    return f'{formatted_time} ({gmt_label})'
