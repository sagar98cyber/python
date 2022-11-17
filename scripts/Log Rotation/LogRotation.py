import logging
import logging.handlers as handlers
import datetime
import time

def getCurrentTimeVal():    
    ts = time.time()
    current_val =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return current_val
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)
## Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler = handlers.TimedRotatingFileHandler('normal.log', when='s', interval=2, backupCount=4)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
errorLogHandler = handlers.RotatingFileHandler('error.log', maxBytes=5000, backupCount=0)
errorLogHandler.setLevel(logging.ERROR)
errorLogHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.addHandler(errorLogHandler)

def main():
    while True:    
        time.sleep(1)
        logger.info(getCurrentTimeVal())

main()
