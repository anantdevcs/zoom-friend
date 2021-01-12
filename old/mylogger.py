import logging
from datetime import datetime

LOG_FORMAT= '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='./lumberjack.log',
                    level=logging.DEBUG, 
                    filemode='w',
                    format=LOG_FORMAT
                    )

mylogger = logging.getLogger()

