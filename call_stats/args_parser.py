

"""Module parses arguments."""


import argparse
import logging

logger = logging.getLogger(__name__)


def prepare_args_parser():
    """Create parser and adds arguments.

    Returns:
        an object with attributes.
    """
    parser = argparse.ArgumentParser(description='Call Stats')
    parser.add_argument('--newkey', required=False, help='Set new key', action='store_true')
    parser.add_argument('--newsecret', required=False, help='Set new secret', action='store_true')
    parser.add_argument(
        '--timestamp',
        required=False,
        help='Set date in ISO format, like "2020-12-12"',
        action='store',
        dest='timestamp',
        default='today',
    )
    return parser.parse_args()


def parse_arguments():
    """Return parser and arguments.

    Returns:
        parser and arguments.
    """
    logger.info('Parsed arguments: {0}'.format(prepare_args_parser()))
    return prepare_args_parser()
