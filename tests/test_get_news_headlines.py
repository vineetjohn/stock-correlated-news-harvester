from utils.web_driver import NewsArticleSearchHelper


article_search_helper = NewsArticleSearchHelper()
urls = article_search_helper.get_news("Blackberry Inc", "01/01/2015", "01/01/2017", 1)

print(urls)
