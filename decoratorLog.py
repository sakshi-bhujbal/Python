from functools import wraps
import logging
logging.basicConfig(level=logging.INFO)
import time

def logg(func):
    @wraps(func)
    def wrapper(data):
        logging.info("STarted: %s",func.__name__)
        func(data)
    try:
        print("The files are being downloaded")
    except:
        logging.exception("something went wrong",func.__name__) 
        raise

    return wrapper

@logg
def process(data):
    print("Downloading started........")
    time.sleep(5)
    print("Downloading completed")

process("Files downloading started")