from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import tldextract
import pandas as pd
from datetime import time
from pprint import pprint


# make urls dict for each url, with domain as the key for organization
urls = {
  tldextract.extract("https://techcrunch.com/").domain: "https://techcrunch.com/"
}

# Data to retrieve from each article:
# Title, Author, Image, URL, 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#TODO add another technology news source
for url in urls:
  try:
    driver.get(urls[url])
    articles = driver.find_elements(By.XPATH,'//article[contains(@class, "post-block--featured")]')
    articles_list = {
      "title": [],
      "author": [],
      "image": [],
      "article_url": []
    }
    for article in articles:
      title = article.find_element(By.XPATH, './/a[@class="post-block__title__link"]')
      articles_list["title"].append(title.text)

      author = article.find_element(By.XPATH, './/span[@class="river-byline__authors"]')
      articles_list["author"].append(author.text)

      image = article.find_element(By.XPATH, './/img')
      articles_list["image"].append(image.get_attribute('src'))

      article_url = article.find_element(By.XPATH, './/a')
      articles_list["article_url"].append(article_url.get_attribute('href'))
      
    pprint(articles_list)
  except Exception as err:
    print(err)

driver.quit()








