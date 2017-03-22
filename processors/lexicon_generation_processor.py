from processors.processor import Processor
from utils import log_helper

log = log_helper.get_logger(__name__)


class LexiconGenerationProcessor(Processor):

    def process(self):
        log.info("LexiconGenerationProcessor begun")

        log.info("LexiconGenerationProcessor completed")
