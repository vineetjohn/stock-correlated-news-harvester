from datetime import datetime
from nltk import tokenize

import pandas

from utils import log_helper

date_column_header = 'Date'
price_column_header = 'Adj Close'

log = log_helper.get_logger(__name__)


stop_words = ['[', ']']

def read_stock_history_file(file_path):
    stock_history_df = pandas.read_csv(file_path)
    stock_history_dict = dict()

    for _, row in stock_history_df.iterrows():
        stock_history_dict[datetime.strptime(row[date_column_header], "%Y-%m-%d").date()] = row[price_column_header]

    return stock_history_dict


def clean_document(document_text):

    document_text = tokenize.word_tokenize(document_text)
    document_text = filter(lambda x: x in stop_words, document_text)

    return document_text
