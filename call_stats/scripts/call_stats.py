

"""call stats package."""


import getpass
import keyring

from call_stats.args_parser import parse_arguments
from call_stats.generate_stats import genstats


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

    print(genstats(key, secret, args.timestamp))


if __name__ == '__main__':
    main()
