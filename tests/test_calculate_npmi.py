import json
import telnetlib

from utils.wumpus_helper import calculate_npmi
from utils import log_helper


log = log_helper.get_logger(__name__)

with open("/etc/config/stock-correlated-news-harvester/wumpus_config.json") as wumpus_config_file:
    wumpus_config = json.load(wumpus_config_file)
    wumpus = telnetlib.Telnet(wumpus_config['wumpus_host'], wumpus_config['wumpus_port'])
    if wumpus:
        log.info("Connected successfully")
    else:
        log.error("Error while connecting")
        exit(0)

mi = calculate_npmi(wumpus, "information", "retrieval", 20)
log.info("NPMI: " + str(mi))

wumpus.close()
