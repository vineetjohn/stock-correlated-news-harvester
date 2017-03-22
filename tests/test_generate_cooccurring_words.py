import json

seed_word_file_path = "/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/StockAnalysis/metadata/seed_words.json"

with open(seed_word_file_path) as seed_word_file:
    seed_word_dict = json.load(seed_word_file)


for seed_word in seed_word_dict.keys():
    print(seed_word)

    break
