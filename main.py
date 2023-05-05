"""
Main with simple website scrape
"""

from json import load
from logging import INFO
from logging import basicConfig
from logging import getLogger

from arrow import now
from requests import get
from bs4 import BeautifulSoup

from os.path import exists
from os import makedirs

basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)

DOWNLOADS_FOLDER = './downloads/'
MODE_READ = 'r'
SETTINGS_FILE = './main.json'


def main():
    time_start = now()
    logger.info(msg='started')

    with open(encoding='utf-8', file=SETTINGS_FILE, mode=MODE_READ, ) as input_fp:
        settings = load(fp=input_fp)

    if not exists(DOWNLOADS_FOLDER):
        logger.info(msg='creating output folder: {}'.format(DOWNLOADS_FOLDER), )
        makedirs(name=DOWNLOADS_FOLDER, )

    url = settings['url']
    logger.info(msg='url: {url}'.format(url=url))

    response = get(url=url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.findAll('a')

    logger.info(msg='done; time: {:0.3f}'.format((now() - time_start).seconds))


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        logger.error(exc_info=True, msg='error:')
