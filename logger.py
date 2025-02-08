import logging  

# Save log messages to a file
def log_setup():
    log_format = '%(lineno)d : %(name)s : %(asctime)s : %(message)s  '
    date_format = '%d-%m-%Y %H:%M:%S'
    
    logging.basicConfig(
    filename = "C://Ashish.log",
    level = logging.INFO, 
    filemode = 'a', 
    datefmt = date_format,
    format = log_format)
    
    logger = logging.getLogger("Ashish")
    return logger
    
log = log_setup()

def registration():
    log.info("start the method")
    print("username")
    log.info("insert username")
    print("password")
    log.info("insert password")
    
registration()


# Sequence of logger
#notset("not set message")                  # level 0
log.debug("This is a DEBUG message")            # level 10 
log.info("This is an INFO message")             # level 20
log.warning("This is a WARNING message")        # level 30 by default set
log.error("This is an ERROR message")           # level 40
log.critical("This is a CRITICAL message")      # level 50

## time format


## filemode 
# w = write
# a = append

