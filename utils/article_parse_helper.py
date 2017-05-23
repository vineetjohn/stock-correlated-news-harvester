from newspaper import Article

from utils import log_helper

log = log_helper.get_logger(__name__)


def get_article_content(url_list):
    article_tuples = list()

    for url in url_list:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article_tuple = (article.title, article.text)
            article_tuples.append(article_tuple)
        except Exception as e:
            log.error(e)

    return article_tuples


def get_tweet_content(status_list):
    tweets = list()

    for status in status_list:
        tweets.append(status.text)

    return tweets
