from utils.tweet_search_helper import TweetSearchHelper

tweet_search_helper = TweetSearchHelper("/etc/config/stock-correlated-news-harvester/twitter_config.json")
LEXICON = {
    "pos": ['surge', 'rise', 'jump', 'gain'],
    "neg": ['drop', 'fall', 'plunge', 'slump', 'shrink']
}


news = tweet_search_helper.get_news("Blackberry", "2015-11-01", "2017-05-30", LEXICON["pos"])

print(news)
for status in news:
    print(status.text)
