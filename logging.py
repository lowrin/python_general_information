################################################################################################################################
## logging
import logging
# to console and file
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("logs/log1.log"),
                              logging.StreamHandler()])
################################################################################################################################