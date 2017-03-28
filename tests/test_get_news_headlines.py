from utils.article_search_helper import NewsArticleSearchHelper


article_search_helper = NewsArticleSearchHelper()
urls = article_search_helper.get_news("Blackberry", "01/01/2015", "01/01/2017", 3,
                                      ['drop', 'fall', 'plunge', 'slump', 'shrink'])

print(urls)
