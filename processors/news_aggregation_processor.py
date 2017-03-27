import json
import statistics
from os import walk

from processors.processor import Processor
from utils import file_helper
from utils import log_helper
from utils import stat_analysis_helper

log = log_helper.get_logger(__name__)
STOCK_HISTORY_FILE_PREFIX = "STOCK_HISTORY_"
STOCK_HISTORY_FILE_SUFFIX = ".csv"

class NewsAggregationProcessor(Processor):

    def process(self):
        log.info("NewsAggregationProcessor begun")

        # list all files
        stock_history_files = list()
        for (dirpath, dirnames, filenames) in walk(self.options.stock_histories_file_path):
            stock_history_files.extend(filenames)
        stock_history_files = \
            list(map(lambda x: self.options.stock_histories_file_path + "/" + x, stock_history_files))

        with open(self.options.stock_symbol_mapping_file_path) as stock_symbol_mapping_file:
            stock_symbol_mapping = json.load(stock_symbol_mapping_file)

        # mapper function for each file to a function
        list(map(lambda x: process_org_stock_history(x, stock_symbol_mapping), stock_history_files))

        log.info("NewsAggregationProcessor completed")


def process_org_stock_history(stock_history_file, stock_symbol_mapping):

    org_symbol = stock_history_file.split(STOCK_HISTORY_FILE_PREFIX)[1].split(STOCK_HISTORY_FILE_SUFFIX)[0]
    if org_symbol in stock_symbol_mapping.keys():
        org_name = stock_symbol_mapping[org_symbol]
    else:
        return

    log.info("Reading stock history")
    stock_history_dict = file_helper.read_stock_history_file(stock_history_file)

    log.info("Calculating first order differences")
    first_order_differences = stat_analysis_helper.calculate_first_order_differential(stock_history_dict)

    price_difference = first_order_differences.values()
    price_mean = statistics.mean(price_difference)
    price_std = statistics.stdev(price_difference)
    log.debug("price_mean: " + str(price_mean))
    log.debug("price_std: " + str(price_std))

    good_days = list()
    bad_days = list()
    for date in first_order_differences.keys():
        if first_order_differences[date] > price_mean + (2 * price_std):
            good_days.append(date)
        elif first_order_differences[date] < -1 * (price_mean + (2 * price_std)):
            bad_days.append(date)

    log.debug(str(len(good_days)) + " good days")
    log.debug(str(len(bad_days)) + " bad days")
