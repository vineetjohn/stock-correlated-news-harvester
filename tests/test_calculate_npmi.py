import json
import telnetlib

from utils.wumpus_helper import calcMI
from utils import log_helper


log = log_helper.get_logger("test_calculate_npmi")

with open("/home/v2john/Projects/stock-correlated-news-harvester/config/wumpus_config.json") as wumpus_config_file:
    wumpus_config = json.load(wumpus_config_file)
    wumpus = telnetlib.Telnet(wumpus_config['wumpus_host'], wumpus_config['wumpus_port'])
    if wumpus:
        log.info("Connected successfully")
    else:
        log.error("Error while connecting")
        exit(0)

mi = calcMI(wumpus, "information", "retrieval", 20)
log.info("NPMI: " + str(mi))

wumpus.close()
