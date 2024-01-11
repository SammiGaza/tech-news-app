SITE_CONFIGS = {
  'TechCrunch': {
    'url': 'https://techcrunch.com/',
    'article_list_xpath': '//*[@id="tc-main-content"]/div[3]/div/div/div',
    # 'title text stored in 'a' element
    'title_xpath': '//article/header/h2/a/text()',
    # author text stored in 'a' element
    'author_xpath': '//article/header/div[2]/div/span/span/a/text()', 
    'image_xpath': '//article/footer/figure/picture/img/@src',
    'article_url_xpath': '//article/header/h2/a/@href',
    'date_xpath': '//article/header/div[2]/div/div/time/@datetime',
  },
  # Wired.com - Today's picks
  'Wired_Variation1': {
    'url': 'https://www.wired.com/',
    'article_list_xpath': '//*[@id="today’s-picks"]/section/div[2]/div[2]/div[2]/div/div/div',
    # title text stored in h2 element
    'title_xpath': '//div/div[2]/a/h2/text()',
    # author text stored in span element
    'author_xpath': '//div/div[2]/div[2]/div/div/div/p/span/span/text()',
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
    'title_xpath': '//div[1]/div[2]/a/h2/text()',
    # author text in span element
    'author_xpath': '//div[1]/div[2]/div[3]/div/div/div/p/span/span/text()',
    # image in src attribute
    'image_xpath': '//div[1]/div[1]/a/span/div/div/picture/img/@src',
    'article_url_xpath': '//div[1]/div[2]/a/@href',
    'date_xpath': '',
  },
  # Wired.com - Latest feed
  'Wired_Variation3': {
    'url': 'https://www.wired.com/',
    'article_list_xpath': '//*[@id="today’s-picks"]/section/div[3]/div/div/div/div',
    'title_xpath': '//div/div[2]/a/h2/text()',
    'author_xpath': '//div/div[2]/div/div/div/div/p/span/span/text()',
    'image_xpath': '//div/div[1]/a/span/picture/img/@src',
    'article_url_xpath': '//div/div[2]/a/@href',
    'date_xpath': '',
  },
  # Business Insider - Front of Homepage
  'BusinessInsider_Variation1': {
    'url': 'https://www.businessinsider.com/tech',
    'article_list_xpath': '//*[@id="l-main-content"]/section/section/div/section',
    'title_xpath': '//div/h2/a/text()',
    'author_xpath': '',
    'image_xpath': '//div/a/div/img/@src',
    'article_url_xpath': 'div/h2/a/@href',
    'date_xpath': '//div/div[1]/span/text()',
  },
  # Business Insider - Homepage Latest Feed
  'BusinessInsider_Variation2': {
    'url': 'https://www.businessinsider.com/tech',
    'article_list_xpath': '//*[@id="l-content"]',
    'title_xpath': '//section/section/div[2]/h2/a/text()',
    'author_xpath': '',
    'image_xpath': '//section/section/div[1]/a/div/img/@src',
    'article_url_xpath': 'section/section/div[2]/h2/a/@href',
    'date_xpath': '//section/div/span/text()',
  },
  # Popular Now cover on homepage
  'Engadget_Variation1': {
    'url': 'https://www.engadget.com/',
    'article_list_xpath': '//*[@id="module-dynamic-lede"]/div/section/div/div[2]/div[1]/div[2]',
    'title_xpath': '//div/a/h1/text()',
    'author_xpath': '',
    'image_xpath': '//div/a/div[1]/img/@src',
    'article_url_xpath': '//div/a/@href',
    'date_xpath': '//div/a/div[2]/text()',
  },
  # Front cover of homepage
  'Engadget_Variation2': {
    'url': 'https://www.engadget.com/',
    'article_list_xpath': '//*[@id="module-dynamic-lede"]/div/section/div/div[2]/div[2]/div[1]',
    'title_xpath': '//div/article/div/div/div/div/h2/a/text()',
    'author_xpath': '//div/article/div/div/div/div/div[2]/div[1]/a/div/text()',
    'image_xpath': '//div/article/div/a/div/img/@src',
    'article_url_xpath': '//div/article/div/div/div/div/h2/a/@href',
    'date_xpath': '//div/article/div/div/div/div/div[2]/div[1]/a/div/text()',
  },
  # right side feed of homepage
  'Engadget_Variation3': {
    'url': 'https://www.engadget.com/',
    'article_list_xpath': '//*[@id="module-dynamic-lede"]/div/section/div/div[2]/div[2]/div[2]',
    'title_xpath': '//div/article/div/div/div/div/h2/a/text()',
    'author_xpath': '//div/article/div/div/div/div/div/div[1]/a/div/text()',
    'image_xpath': '//div/article/div/a/div/img/@src',
    'article_url_xpath': '//div/article/div/div/div/div/h2/a/@href',
    'date_xpath': '//div/article/div/div/div/div/div/div[1]/a/div/span[2]/text()',
  },
  # Latest feed
  'Engadget_Variation4': {
    'url': 'https://www.engadget.com/',
    'article_list_xpath': '//*[@id="module-latest"]/div/div/div/div[2]/div[1]/ul',
    'title_xpath': '//li/article/div/div/div/div/h2/a/text()',
    'author_xpath': '//li/article/div/div/div/div/div[2]/div[1]/a/div/text()',
    'image_xpath': '//li/article/div/a/img/@src',
    'article_url_xpath': '//li/article/div/div/div/div/h2/a/@href',
    'date_xpath': '//li/article/div/div/div/div/div[2]/div[1]/a/div/span[2]/text()',
  },
  # Tech page featured articles
  'TheVerge_Variation1': {
    'url': 'https://www.theverge.com/tech',
    'article_list_xpath': '//*[@id="content"]/div/section/div',
    'title_xpath': '//div/div[2]/h2/a/text()',
    'author_xpath': '//div/div[2]/div/div[1]/a/text()',
    'image_xpath': '//div/div[1]/div/div[1]/a/span/img/@src',
    'article_url_xpath': '//div/div[2]/h2/a/@href',
    'date_xpath': '//div/div[2]/div/div[2]/time/@datetime',
  },
  # Tech page Most Popular feed
  'TheVerge_Variation2': {
    'url': 'https://www.theverge.com/tech',
    'article_list_xpath': '//*[@id="content"]/div/div[3]/div/div[2]/div[2]/div/ol',
    'title_xpath': '//li/a/h2/text()',
    'author_xpath': '',
    'image_xpath': '',
    'article_url_xpath': '//li/a/@href',
    'date_xpath': '',
  },
}


