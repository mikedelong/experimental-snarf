"""
Selenium demo
"""

from logging import INFO
from logging import basicConfig
from logging import getLogger

from arrow import now
from selenium import webdriver

ARGUMENTS = [
    '--disable-extensions',
    '--disable-infobars',
    '--disable-dev-shm-usage',
    '--disable-browser-side-navigation',
    '--ignore-certificate-errors',
    '--no-sandbox',
    '--remote-debugging-port=9222',
    '--test-type'
]
EXECUTABLE_PATH = '/usr/bin/chromedriver'
URL = 'https://www.google.com/'
basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)


def main():
    time_start = now()
    logger.info(msg='started')

    options = webdriver.ChromeOptions()
    for argument in ARGUMENTS:
        options.add_argument(argument=argument)
    options.binary_location = '/usr/bin/chromium-browser'

    driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    driver.get(url=URL)

    logger.info(msg='done; time: {:0.3f}'.format((now() - time_start).seconds))


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        logger.error(exc_info=True, msg='error:')
