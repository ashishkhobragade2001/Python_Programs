from logging import *

# Save log messages to a file
def log_setup():
    log_format = '%(lineno)s :%(name)s : %(asctime)s : %(message)s  '
    date_format = '%d-%m-%Y %H:%M:%S'
    
    basicConfig(
    filename="Ashish.log",
    level=DEBUG, 
    filemode='w', 
    datefmt=date_format,
    format=log_format)
    
    logger = getLogger("Ashish")
    return logger
logger = log_setup()
# Sequence of logger
#notset("not set message")                  # level 0
logger.debug("This is a DEBUG message")     # level 10 
logger.info("This is an INFO message")             # level 20
logger.warning("This is a WARNING message")        # level 30 by default set
logger.error("This is an ERROR message")           # level 40
logger.critical("This is a CRITICAL message")      # level 50

## time format


## filemode 
# w= write
# a = append

