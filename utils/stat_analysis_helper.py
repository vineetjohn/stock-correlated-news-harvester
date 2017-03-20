from datetime import timedelta


def calculate_first_order_differential(stock_history_dict):
    first_order_diff_dict = dict()
    sorted_date_list = list(sorted(stock_history_dict.keys()))
    for i in range(1, len(sorted_date_list)):
        delta = sorted_date_list[i] - sorted_date_list[i-1]
        if delta == timedelta(days=1):
            first_order_diff_dict[sorted_date_list[i]] = \
                stock_history_dict[sorted_date_list[i]] - stock_history_dict[sorted_date_list[i-1]]

    return first_order_diff_dict
