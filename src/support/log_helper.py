from support.path_helper import *
import datetime
import logging as lg
import sys
import os

LOG_DIR = from_root('log/', create_if_needed=True)[:-1]


def _get_fpath(name):
    cur_date = datetime.datetime.now().strftime("%y-%m-%d")
    cur_time = datetime.datetime.now().strftime("%H-%M-%S")
    return f'{LOG_DIR}/{name}_{cur_date}_{cur_time}.log'


def get_logger(name):
    return lg.getLogger(name)

def init_logger(name, log_to_file=True, log_to_stdout=True, level=lg.DEBUG):
    logger = lg.getLogger(name)

    if len(logger.handlers) == 0:
        close_logger(name)

    formatter = lg.Formatter('%(asctime)s  %(levelname)8s  %(name)35s >>> %(message)s')

    if log_to_file:
        fpath = _get_fpath(name)
        file_handler = lg.FileHandler(fpath)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if log_to_stdout:
        stream_handler = lg.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    logger.setLevel(level)
    logger.debug('Logger {} initialized'.format(name))        

    return logger


def close_logger(name):
    logger = lg.getLogger(name)

    for h in logger.handlers:
        h.close()
    logger.handlers.clear()


if __name__ == "__main__":
    logger = init_logger('test')
    logger.info('hello')