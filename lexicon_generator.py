from argparse import ArgumentParser

import sys

from processors.lexicon_generation_processor import LexiconGenerationProcessor
from utils import log_helper
from utils.options import Options

log = log_helper.get_logger(__name__)


def main(argv):
    options = parse_args(argv)
    # log.info("options: " + str(options))

    processor = LexiconGenerationProcessor(options)
    processor.process()


def parse_args(argv):
    parser = ArgumentParser(prog="lexicon-generator")
    return parser.parse_args(argv, namespace=Options())


if __name__ == "__main__":
    main(sys.argv[1:])
