from time import sleep
from newspaper import Article

from utils import log_helper

log = log_helper.get_logger(__name__)


def get_article_content(url_list):
    article_tuples = list()

    for url in url_list:
        try:
            article = Article(url)
            article.download()
            sleep(1)
            article.parse()
            article_tuple = (article.title, article.text)
            article_tuples.append(article_tuple)
        except Exception as e:
            log.error(e)

    return article_tuples
