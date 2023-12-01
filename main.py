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


def open_spreadsheet(gc, config):
    logging.info("Opening spreadsheet")
    spreadsheet = gc.open(config.spreadsheet)
    logging.info("Spreadsheet opened")
    return spreadsheet


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


def batch_read(spreadsheet, config):
    logging.info("Batch reading")
    worksheets = config.get_worksheets()
    google_worksheets = []

    logging.info("Creating list of worksheets: ")
    for worksheet in worksheets:
        google_worksheets.append(spreadsheet.worksheet_by_title(worksheet))

    logging.info("List of worksheets created")

    # Fetch all B11 values from each worksheet
    logging.info("Fetching all B11 values from each worksheet")

    last_pinged_list = []
    for worksheet in google_worksheets:
        logging.info("Fetching all B11 values from " + worksheet.title)
        last_pinged_list.append(worksheet.get_value('B11'))
        logging.info("Fetched all B11 values from " + worksheet.title)

    logging.info("All B11 values fetched")
    return last_pinged_list


def pinged_availability(last_pinged_list ):
    logging.info("Checking availability of each server")

    for last_pinged in last_pinged_list:
        get_availability(last_pinged)


if __name__ == '__main__':
    start_time = time.time()

    config = Config()
    retrieve_config_values(config)

    gc = authorize()

    spreadsheet = open_spreadsheet(gc, config)

    last_pinged_list = batch_read(spreadsheet, config)
    #print(last_pinged_list)
    availability_list = pinged_availability(last_pinged_list)


    #batch_read(spreadsheet, config)

    print("--- %s seconds ---" % (time.time() - start_time))
