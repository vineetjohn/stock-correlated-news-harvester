from processors.processor import Processor
from utils import log_helper

log = log_helper.get_logger("NewsAggregationProcessor")


class NewsAggregationProcessor(Processor):

    def process(self):
        log.info("NewsAggregationProcessor begun")

        log.info("NewsAggregationProcessor completed")
