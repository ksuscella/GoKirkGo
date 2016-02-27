import time

arg_decisions = 100
tracker = 0

def robot():
    while True:
        time.sleep(5)
        tracker = tracker + 1
        if tracker > arg_decisions:
            break
    
def getCount():
    return tracker
## create logger
#logger = logging.getLogger('simple_example')
#logger.setLevel(logging.DEBUG)

## create console handler and set level to debug
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)

## create formatter
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

## add formatter to ch
#ch.setFormatter(formatter)

## add ch to logger
#logger.addHandler(ch)

## 'application' code
#logger.debug('debug message')
#logger.info('info message')
#logger.warn('warn message')
#logger.error('error message')
#logger.critical('critical message')

