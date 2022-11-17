import datetime
import logging
import logging.handlers as handlers
import os
import time


def getCurrentTimeVal():    
    ts = time.time()
    current_val =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return current_val

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)
logHandler = handlers.TimedRotatingFileHandler('timed.log', when='M', interval=1,backupCount=4)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)
def main():
    while True:
        time.sleep(1)
        #logger.info("A Sample Log Statement")
        logger.info(getCurrentTimeVal())

main()