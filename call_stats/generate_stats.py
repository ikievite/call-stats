

"""Module generates call stats."""


import logging
import requests
import datetime


logger = logging.getLogger(__name__)


def get_json(url, payload):
    """Get json.

    Args:
        url: url
        payload: dict with auths data and timestamp

    Returns:
        json
    """
    return requests.post(url, json=payload).json()


def mkstamp(timestamp):
    """Make unix timestamp.

    Args:
        timestamp: timestamp

    Returns:
        unux timestamp
    """
    if timestamp == 'today':
        date = datetime.date.today()
    else:
        date = datetime.date.fromisoformat(timestamp)

    time = datetime.time(0, 0)
    dt = datetime.datetime.combine(date, time)
    return datetime.datetime.timestamp(dt)


def genstats(auth_key, auth_secret, timestamp):
    """Generate call stats.

    Args:
        auth_key: key
        auth_secret: secret
        timestamp: timestamp

    Returns:
        stats
    """
    url = 'https://api.binotel.com/api/4.0/stats/all-incoming-calls-since.json'

    unix_stamp = mkstamp(timestamp)

    payload = {
        'timestamp': unix_stamp,
        'key': auth_key,
        'secret': auth_secret,
    }

    return get_json(url, payload)
