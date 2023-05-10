"""
Main with simple website scrape
"""

from json import load
from logging import INFO
from logging import basicConfig
from logging import getLogger
from os import makedirs
from os.path import basename
from os.path import exists

from arrow import now
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver

basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)

ARGUMENTS = ['--enable-cookies', '--enable-javascript', ]
DOWNLOADS_FOLDER = './downloads/'
EXECUTABLE_PATH = '/usr/bin/chromedriver'
HTML_FOLDER = './html/'
MODE_READ = 'r'
MODE_WRITE = 'w'
MODE_WRITE_BINARY = 'wb'
SETTINGS_FILE = './main.json'


def images(url: str, folder: str):
    response = get(url=url, )
    soup = BeautifulSoup(markup=response.content, features='html.parser', )
    tags = soup.findAll(name='img', )
    for tag in tags:
        image_url = tag.get('src')
        image_response = get(url=image_url, )
        image_filename = basename(image_url)
        with open(file=folder + image_filename, mode=MODE_WRITE_BINARY) as output_fp:
            output_fp.write(image_response.content)


def main():
    time_start = now()
    logger.info(msg='started')

    with open(encoding='utf-8', file=SETTINGS_FILE, mode=MODE_READ, ) as input_fp:
        settings = load(fp=input_fp)

    for folder in [DOWNLOADS_FOLDER, HTML_FOLDER]:
        if not exists(folder):
            logger.info(msg='creating folder: {}'.format(folder), )
            makedirs(name=folder, )

    url = settings['url']
    logger.info(msg='url: {url}'.format(url=url))

    # let's get the content from the URL first
    options = webdriver.ChromeOptions()
    for argument in ARGUMENTS:
        options.add_argument(argument=argument)
    options.headless = False

    with webdriver.Chrome(options=options) as driver:
        driver.get(url=url, )
        page_source = driver.page_source
        driver.implicitly_wait(0)
    driver.quit()
    logger.info(msg='page source length: {}'.format(len(page_source)))
    logger.info(msg='done; time: {:0.3f}'.format((now() - time_start).seconds))
    return page_source


if __name__ == '__main__':
    try:
        t = main()
    except Exception as exception:
        logger.error(exc_info=True, msg='error:')
