from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import time
from pprint import pprint


# Grab page to scrape then parse with bs4
url = "https://techcrunch.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
# get title, author, image, url


  







