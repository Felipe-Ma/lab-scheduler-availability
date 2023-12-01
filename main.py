import pygsheets
import time
import logging
from functions import *

# Log in terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


def authorize():
    logging.info("Authorizing Google Sheets API")
    gc = pygsheets.authorize(service_file="testing.json")

    return gc

    #logging.info("Opening spreadsheet 1")
    #spreadsheet = gc.open("Server Dashboard")


def retrieve_config_values(config):
    #config()
    logging.info("Retrieving config values")
    config.set_current_directory(get_current_directory())
    config.set_config_path(get_config_path(config.current_directory))
    config.set_credential_path(get_credential_path(config.config_path))
    config.set_spreadsheet(get_spreadsheet(config.config_path))
    config.set_worksheets(get_worksheets(config.config_path))
    logging.info("Config values retrieved")
    #config()


if __name__ == '__main__':
    start_time = time.time()

    config = Config()
    retrieve_config_values(config)

    gc = authorize()

    print("--- %s seconds ---" % (time.time() - start_time))
