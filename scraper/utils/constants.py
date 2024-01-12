from bs4 import BeautifulSoup
from selenium import webdriver


# defaults for Selenium
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument('--headless')
CHROME_OPTIONS.add_argument('incognito')
CHROME_OPTIONS.add_experimental_option('detach', True)
DEFAULT_WAIT = 10


#defaults for BeautifulSoup
BEAUTIFUL_SOUP_PARSER = 'html.parser'
