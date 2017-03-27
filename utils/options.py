class Options(object):
    stock_histories_file_path = None
    stock_symbol_mapping_file_path = None
    results_path = None

    def __repr__(self):
        return \
            "stock_file_path: " + self.stock_histories_file_path + ", " \
            "stock_symbol_mapping_file_path: " + self.stock_symbol_mapping_file_path + ", " \
            "results_path: " + self.results_path
