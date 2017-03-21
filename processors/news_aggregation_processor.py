import statistics

from processors.processor import Processor
from utils import file_helper
from utils import log_helper
from utils import stat_analysis_helper

log = log_helper.get_logger("NewsAggregationProcessor")


class NewsAggregationProcessor(Processor):

    def process(self):
        log.info("NewsAggregationProcessor begun")

        log.info("Reading stock history")
        stock_history_dict = file_helper.read_stock_history_file(self.options.stock_file_path)

        log.info("Calculating first order differences")
        first_order_differences = stat_analysis_helper.calculate_first_order_differential(stock_history_dict)
        print(len(first_order_differences))

        price_difference = first_order_differences.values()
        price_mean = statistics.mean(price_difference)
        price_std = statistics.stdev(price_difference)

        log.info("price_mean: " + str(price_mean))
        log.info("price_std: " + str(price_std))

        good_days = list()
        bad_days = list()
        for date in first_order_differences.keys():
            if first_order_differences[date] > price_mean + (2 * price_std):
                good_days.append(date)
            elif first_order_differences[date] < -1 * (price_mean + (2 * price_std)):
                bad_days.append(date)

        log.debug(str(len(good_days)) + " good days")
        log.debug(str(len(bad_days)) + " bad days")

        log.info("NewsAggregationProcessor completed")
