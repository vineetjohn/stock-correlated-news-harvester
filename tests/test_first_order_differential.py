from utils import file_helper
from utils import stat_analysis_helper

stock_file_path = \
    "/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/stockhistories/STOCK_HISTORY_BB.csv"

stock_history_dict = file_helper.read_stock_history_file(stock_file_path)
first_order_differences = stat_analysis_helper.calculate_first_order_differential(stock_history_dict)

print(first_order_differences)
