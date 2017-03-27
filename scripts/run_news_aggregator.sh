#!/usr/bin/env bash

CODEDIR=$(dirname "$0")"/../"
STOCK_FILE_PATH="/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/stockhistories/"

/usr/bin/python3 "$CODEDIR"/stock_correlated_news_harvester.py \
--stock_histories_file_path "$STOCK_FILE_PATH" \
--stock_symbol_mapping_file_path /home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/metadata/symbol_mapping.json \
--results_path /home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/annotated-articles/
