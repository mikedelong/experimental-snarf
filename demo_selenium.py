"""
Selenium demo
"""

from logging import INFO
from logging import basicConfig
from logging import getLogger

from arrow import now
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

ARGUMENTS = [
    '--disable-extensions',
    '--disable-infobars',
    '--disable-dev-shm-usage',
    '--disable-browser-side-navigation',
    '--no-sandbox',
    '--remote-debugging-port=9222',
]
URL = 'https://www.google.com/'
basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)


def main():
    time_start = now()
    logger.info(msg='started')

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--test-type')
    options.binary_location = '/usr/bin/chromium-browser'

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
    driver.get('https://python.org')

    logger.info(msg='done; time: {:0.3f}'.format((now() - time_start).seconds))


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        logger.error(exc_info=True, msg='error:')
