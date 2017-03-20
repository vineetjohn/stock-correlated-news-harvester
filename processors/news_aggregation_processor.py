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

        log.info("NewsAggregationProcessor completed")
