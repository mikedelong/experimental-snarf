"""
Main with simple website scrape
"""

from logging import INFO
from logging import basicConfig
from logging import getLogger

basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)


def main():
    logger.info(msg='started')


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        logger.error(exc_info=True, msg='error:')
