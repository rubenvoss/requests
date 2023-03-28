import logging
from datetime import datetime

def setup_logger(name, log_file, level=logging.DEBUG):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

file1 = "/Users/ruben/code/requests/requests_1.log"
file2 = "/Users/ruben/code/requests/requests_2.log"

logger_1 = setup_logger('logger_1', file1)
logger_2 = setup_logger('logger_2', file2)


def info_log(log):
    logger_1.info(log)
    logger_2.info(log)

def debug_log(log):
    logger_1.debug(log)
    logger_2.debug(log)

def exception_log(log):
    logger_1.exception(log)
    logger_2.exception(log)
