import json
import telnetlib

from utils import wumpus_helper

seed_word_file_path = "/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/metadata/seed_words.json"

with open(seed_word_file_path) as seed_word_file:
    seed_word_dict = json.load(seed_word_file)


with open("/etc/config/stock-correlated-news-harvester/wumpus_config.json") as wumpus_config_file:
    wumpus_config = json.load(wumpus_config_file)
    wumpus = telnetlib.Telnet(wumpus_config['wumpus_host'], wumpus_config['wumpus_port'])
    if wumpus:
        print("Connected successfully")
    else:
        print("Error while connecting")
        exit(0)

for seed_word in seed_word_dict.keys():
    results = wumpus_helper.get_stock_relevant_docs(wumpus, seed_word)

    break
