from selenium import webdriver
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


MODE_READ = 'r'
SETTINGS_FILE = './main.json'

basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)

with open(encoding='utf-8', file=SETTINGS_FILE, mode=MODE_READ, ) as input_fp:
    settings = load(fp=input_fp)

url = settings['url']
logger.info(msg='url: {url}'.format(url=url))

options = webdriver.ChromeOptions()
for argument in [
    '--enable-cookies',
    '--enable-javascript'
]:
    options.add_argument(argument=argument)
options.headless = False

with webdriver.Chrome(options=options) as driver:
    driver.get(url=url, )
    page_source = driver.page_source
    driver.implicitly_wait(1)
driver.quit()

print(len(page_source))
