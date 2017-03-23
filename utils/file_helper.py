import enchant
from datetime import datetime
from nltk import tokenize
from nltk.corpus import stopwords

import pandas

from utils import log_helper

date_column_header = 'Date'
price_column_header = 'Adj Close'
dictionary = enchant.Dict("en_US")

log = log_helper.get_logger(__name__)


def read_stock_history_file(file_path):
    stock_history_df = pandas.read_csv(file_path)
    stock_history_dict = dict()

    for _, row in stock_history_df.iterrows():
        stock_history_dict[datetime.strptime(row[date_column_header], "%Y-%m-%d").date()] = row[price_column_header]

    return stock_history_dict


def clean_document(document_text):
    document_text = tokenize.word_tokenize(document_text.lower())
    document_text = list(filter(lambda x: check_word_validity(x), document_text))

    return document_text


def check_word_validity(word):
    return word.isalpha() and dictionary.check(word) and word not in stopwords.words('english')
