

"""Call Stats Project."""


import logging

from call_stats.generate_stats import genstats

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '{asctime} - {levelname} - {name} - {message}', datefmt='%H:%M:%S', style='{',
)

console.setFormatter(formatter)

logger.addHandler(console)


__all__ = (  # noqa: WPS410
    'genstats',
)
