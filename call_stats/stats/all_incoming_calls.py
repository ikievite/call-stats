

"""Stats about incoming calls."""


import datetime

import requests


def all_in_calls(key, secret):
    """Fing all incoming calls since date.

    Args:
        key: for api
        secret: for api

    Returns:
        json with all incoming calls since date
    """
    url = 'https://api.binotel.com/api/4.0/stats/all-incoming-calls-since.json'
    date = datetime.date.today()
    time = datetime.time(0, 0)
    dt = datetime.datetime.combine(date, time)
    timestamp = datetime.datetime.timestamp(dt)

    payload = {
        'timestamp': timestamp,
        'key': key,
        'secret': secret,
    }
    if key and secret:
        output = requests.post(url, json=payload)
        return output.json()
