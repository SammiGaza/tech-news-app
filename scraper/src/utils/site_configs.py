SITE_CONFIGS = {
  'TechCrunch': {
    'url': 'https://techcrunch.com/',
    'article_list_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div',
    # 'title text stored in 'a' element
    'title_xpath': '//article/header/h2/a',
    # author text stored in 'a' element
    'author_xpath': '//article/header/div[2]/div/span/span/a', 
    'image_xpath': '//article/footer/figure/picture/img/@src',
    'article_url_xpath': '//article/header/h2/a/@href',
    'date_xpath': '//article/header/div[2]/div/div/time/@datetime',
  },
  # Wired.com - Today's picks
  'Wired_Variation1': {
    'url': 'https://www.wired.com/',
    'article_list_xpath': '//*[@id="today’s-picks"]/section/div[2]/div[2]/div[2]/div/div/div',
    # title text stored in h2 element
    'title_xpath': '//div/div[2]/a/h2',
    # author text stored in span element
    'author_xpath': '//div/div[2]/div[2]/div/div/div/p/span/span',
    # image stored in src attribute
    'image_xpath': '//div/div[1]/a/span/div/div/picture/img/@src',
    # url stored in href attribute
    'article_url_xpath': '//div/div[2]/a/@href',
    'date_xpath': '',
  },
  # Wired.com - front cover on homepage
  'Wired_Variation2': {
    'url': 'https://www.wired.com/',
    'article_list_xpath': '//*[@id="today’s-picks"]/section/div[2]/div[2]',
    # title text in h2 element
    'title_xpath': '//div[1]/div[2]/a/h2',
    # author text in span element
    'author_xpath': '//div[1]/div[2]/div[3]/div/div/div/p/span/span',
    # image in src attribute
    'image_xpath': '//div[1]/div[1]/a/span/div/div/picture/img/@src',
    'article_url_xpath': '//div[1]/div[2]/a/@href',
    'date_xpath': '',
  },
  # Wired.com - Most recents
  'Wired_Variation3': {
    'url': 'https://www.wired.com/',
    'article_list_xpath': '//*[@id="today’s-picks"]/section/div[3]/div/div/div/div',
    # title text in h2 element
    'title_xpath': '//div/div[2]/a/h2',
    # author text in span element
    'author_xpath': '//div/div[2]/div/div/div/div/p/span/span',
    # image in src attribute
    'image_xpath': '//div/div[1]/a/span/picture/img/@src',
    'article_url_xpath': '//div/div[2]/a',
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


