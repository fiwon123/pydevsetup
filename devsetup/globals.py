from devsetup.config import load_config
CONFIG = load_config()

LOGGER = None

def get_logger():
    return LOGGER

def set_logger(new_logger):
    global LOGGER
    LOGGER = new_logger