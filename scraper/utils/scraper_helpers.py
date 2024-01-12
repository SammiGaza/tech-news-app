from constants import BEAUTIFUL_SOUP_PARSER
from bs4 import BeautifulSoup

# pass in Selenium page source and parse with BeautifulSoup
def parse_url(page_source):
  try:
    soup = BeautifulSoup(page_source, BEAUTIFUL_SOUP_PARSER)
    

  except Exception as err:
    print(f'{page_source} could not be parsed')




