from utils.tweet_search_helper import TweetSearchHelper

tweet_search_helper = TweetSearchHelper("/etc/config/stock-correlated-news-harvester/twitter_config.json")

news = tweet_search_helper.get_news("Blackberry", "2013-11-01", "2015-04-30", None)

print(news)
for status in news:
    print(status)
