import json
import telnetlib

from utils import wumpus_helper

seed_word_file_path = "/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/metadata/seed_words.json"
augmented_words_file_path = "/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/seed-word-augmentation/"

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
    results = wumpus_helper.get_colocated_words_and_npmi(wumpus, seed_word, seed_word_dict[seed_word])

    print("Completed for " + seed_word + " dumping to file")
    with open(augmented_words_file_path + "augmented_" + seed_word + ".json", "w") as augmented_words_file:
        json.dump(results, augmented_words_file, sort_keys=True, indent=4, separators=(',', ': '))
