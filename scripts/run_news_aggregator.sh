#!/usr/bin/env bash

CODEDIR=$(dirname "$0")"/../"
STOCK_FILE_PATH="/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/stockhistories/STOCK_HISTORY_BB.csv"

/usr/bin/python3 "$CODEDIR"/stock_correlated_news_harvester.py --stock_file_path "$STOCK_FILE_PATH"
