import logging
import logging.handlers as handlers
import time

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

logHandler = handlers.TimedRotatingFileHandler('timed.log', when='S', interval=1)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")

main()