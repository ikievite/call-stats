

"""call stats package."""


import argparse
import getpass
import datetime
import requests  # noqa: I001

import keyring


def parse_arguments():
    """Parse aruments.

    Returns:
        entered arguments
    """
    parser = argparse.ArgumentParser(description='Call Stats')
    parser.add_argument('--newkey', required=False, help='Set new key', action='store_true')
    parser.add_argument('--newsecret', required=False, help='Set new secret', action='store_true')
    arguments = parser.parse_args()
    return arguments


def all_in_calls_today(key, secret):
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


def main():  # noqa: WPS210
    """Run main func."""
    args = parse_arguments()

    service = 'api_connect'
    token_key = 'api_key'
    token_secret = 'api_secret'

    if args.newkey:
        key = getpass.getpass(prompt='Enter key:')
        try:
            keyring.set_password(service, token_key, key)
        except Exception as error:
            print('Error: {0}'.format(error))

    if args.newsecret:
        secret = getpass.getpass(prompt='Enter secret:')
        try:
            keyring.set_password(service, token_secret, secret)
        except Exception as error:  # noqa: WPS440
            print('Error: {0}'.format(error))

    key = keyring.get_password(service, token_key)
    secret = keyring.get_password(service, token_secret)

    print(all_in_calls_today(key, secret))


if __name__ == '__main__':
    main()