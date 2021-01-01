

"""Stats about incoming calls."""


import datetime

import requests


def all_in_calls(key, secret, timestamp):
    """Fing all incoming calls since date.

    Args:
        key: for api
        secret: for api
        timestamp: since that time

    Returns:
        json with all incoming calls since date
    """
    url = 'https://api.binotel.com/api/4.0/stats/all-incoming-calls-since.json'

    if timestamp == 'today':
        date = datetime.date.today()
    else:
        date = datetime.date.fromisoformat(timestamp)

    time = datetime.time(0, 0)
    dt = datetime.datetime.combine(date, time)
    stamp = datetime.datetime.timestamp(dt)

    payload = {
        'timestamp': stamp,
        'key': key,
        'secret': secret,
    }

    if key and secret:
        output = requests.post(url, json=payload)
        return output.json()
