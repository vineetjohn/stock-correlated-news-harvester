import json

import twitter

from utils import log_helper

log = log_helper.get_logger(__name__)


class TweetSearchHelper(object):

    def __init__(self, twitter_config_file_path):
        with open(twitter_config_file_path) as twitter_config_file:
            self.twitter_config = json.load(twitter_config_file)
        self.twitter_api = \
            twitter.Api(consumer_key=self.twitter_config['consumer_key'],
                        consumer_secret=self.twitter_config['consumer_secret'],
                        access_token_key=self.twitter_config['access_token_key'],
                        access_token_secret=self.twitter_config['access_token_secret'],
                        sleep_on_rate_limit=True)

    def get_news(self, search_term, start_time, end_time, sentiment_word_list):
        search_term = search_term + " " + " OR ".join(sentiment_word_list)
        results = \
            self.twitter_api.GetSearch(
                term=search_term,
                since=start_time,
                until=end_time,
                lang="en"
            )

        return results
