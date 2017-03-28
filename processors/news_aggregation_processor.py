import json
import statistics
from nltk import word_tokenize
from datetime import timedelta
from os import listdir
from os.path import isfile, join

from processors.processor import Processor
from utils import file_helper
from utils import log_helper
from utils import stat_analysis_helper
from utils.article_search_helper import NewsArticleSearchHelper
from utils.article_parse_helper import get_article_content

log = log_helper.get_logger(__name__)

# constants
STOCK_HISTORY_FILE_PREFIX = "STOCK_HISTORY_"
STOCK_HISTORY_FILE_SUFFIX = ".csv"
LEXICON = {
    "pos": ['surge', 'rise', 'jump', 'gain'],
    "neg": ['drop', 'fall', 'plunge', 'slump', 'shrink']
}


class NewsAggregationProcessor(Processor):

    def process(self):
        log.info("NewsAggregationProcessor begun")

        # list all files
        stock_history_files = \
            [join(self.options.stock_histories_file_path, f) for f in listdir(self.options.stock_histories_file_path)
             if isfile(join(self.options.stock_histories_file_path, f))]

        # read symbol mapping files
        with open(self.options.stock_symbol_mapping_file_path) as stock_symbol_mapping_file:
            stock_symbol_mapping = json.load(stock_symbol_mapping_file)

        # mapper function for each file to a function
        article_search_helper = NewsArticleSearchHelper()
        list(
            map(
                lambda x: self.process_org_stock_history(x, stock_symbol_mapping, article_search_helper),
                stock_history_files)
        )

        article_search_helper.destroy()
        log.info("NewsAggregationProcessor completed")

    def process_org_stock_history(self, stock_history_file, stock_symbol_mapping, article_search_helper):

        org_symbol = stock_history_file.split(STOCK_HISTORY_FILE_PREFIX)[1].split(STOCK_HISTORY_FILE_SUFFIX)[0]
        if org_symbol in stock_symbol_mapping.keys():
            org_name = stock_symbol_mapping[org_symbol]
        else:
            return

        log.info("Processing stock history for " + org_name)

        log.info("Reading stock history")
        stock_history_dict = file_helper.read_stock_history_file(stock_history_file)

        log.info("Calculating first order differences")
        first_order_differences = stat_analysis_helper.calculate_first_order_differential(stock_history_dict)

        price_difference = first_order_differences.values()
        price_mean = statistics.mean(price_difference)
        price_std = statistics.stdev(price_difference)
        log.debug("price_mean: " + str(price_mean))
        log.debug("price_std: " + str(price_std))

        days_sentiment = dict()
        for date in first_order_differences.keys():
            if first_order_differences[date] > price_mean + (2 * price_std):
                days_sentiment[date] = "pos"
            elif first_order_differences[date] < -1 * (price_mean + (2 * price_std)):
                days_sentiment[date] = "neg"

        list(
            map(
                lambda x:
                self.aggregate_news(article_search_helper, org_name, x, days_sentiment.get(x)),
                days_sentiment.keys()
            )
        )

    def aggregate_news(self, article_search_helper, org_name, date, sentiment):

        aftermath_date_start = date + timedelta(days=1)
        aftermath_date_end = date + timedelta(days=3)
        news_article_urls = \
            article_search_helper.get_news(
                org_name, aftermath_date_start.strftime("%m/%d/%Y"), aftermath_date_end.strftime("%m/%d/%Y"), 3
            )

        news_content = get_article_content(news_article_urls)

        # log.info("Filtering content based on lexicon")
        # news_content = list(filter(lambda x: self.confirm_news_sentiment(x[0], sentiment), news_content))

        if len(news_content) > 0:
            log.info("Writing content to file")
            list(map(lambda x: self.write_content_to_file(x, aftermath_date_start, org_name, sentiment), news_content))

    def confirm_news_sentiment(self, article_headline, sentiment):
        tokens = set(word_tokenize(article_headline))
        lexicon = LEXICON[sentiment]

        for keyword in lexicon:
            if keyword in tokens:
                return True

        return False

    def write_content_to_file(self, article_content, date, org_name, sentiment):

        file_name = org_name + "_" + date.strftime("%Y-%m-%d") + "_" + sentiment + ".txt"

        with open(self.options.results_path + file_name, 'w') as output_file:
            output_file.write(article_content[0] + "\n")
            output_file.write(article_content[1])
