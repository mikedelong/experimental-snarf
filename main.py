"""
Main with simple website scrape
"""

from logging import INFO
from logging import basicConfig
from logging import getLogger

from arrow import now

from json import load

basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)

MODE_READ = 'r'
SETTINGS_FILE = './main.json'


def main():
    time_start = now()
    logger.info(msg='started')

    with open(encoding='utf-8', file=SETTINGS_FILE, mode=MODE_READ, ) as input_fp:
        settings = load(fp=input_fp)

    url = settings['url']
    logger.info(msg='url: {url}'.format(url=url))

    logger.info('done; time: %0.2f', (now() - time_start).seconds)


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        logger.error(exc_info=True, msg='error:')
