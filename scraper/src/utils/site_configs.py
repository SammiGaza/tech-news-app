SITE_CONFIGS = {
  'TechCrunch': {
    'url': 'https://techcrunch.com/',
    'article_list_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div',
    
    # 'a' link element stores title as its text
    'title_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div/article/header/h2/a',
    # 'a' link element stores authors as its text
    'author_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div/article/header/div[2]/div/span/span/a', 

    'image_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div/article/footer/figure/picture/img/@src',
    'article_url_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div/article/header/h2/a/@href',
    'date_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div/article/header/div[2]/div/div/time/@datetime',
  },
  'Wired': {
    'url': 'https://www.wired.com/',
    'article_list_xpath': '',
    'title_xpath': '',
    'author_xpath': '',
    'image_xpath': '',
    'article_url_xpath': '',
    'date_xpath': '',
  },
  'BusinessInsider': {
    'url': 'https://www.businessinsider.com/tech',
    'article_list_xpath': '',
    'title_xpath': '',
    'author_xpath': '',
    'image_xpath': '',
    'article_url_xpath': '',
    'date_xpath': '',
  },
  'Engadget': {
    'url': 'https://www.engadget.com/',
    'article_list_xpath': '',
    'title_xpath': '',
    'author_xpath': '',
    'image_xpath': '',
    'article_url_xpath': '',
    'date_xpath': '',
  },
  'TheVerge': {
    'url': 'https://www.theverge.com/',
    'article_list_xpath': '',
    'title_xpath': '',
    'author_xpath': '',
    'image_xpath': '',
    'article_url_xpath': '',
    'date_xpath': '',
  },
}


