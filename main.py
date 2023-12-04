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


def open_availability_worksheet(spreadsheet, config):
    logging.info("Opening availability worksheet")
    worksheet = spreadsheet.worksheet_by_title(config.availability_spreadsheet)
    logging.info("Availability spreadsheet worksheet")
    return worksheet

def retrieve_config_values(config):
    #config()
    logging.info("Retrieving config values")
    config.set_current_directory(get_current_directory())
    config.set_config_path(get_config_path(config.current_directory))
    config.set_credential_path(get_credential_path(config.config_path))
    config.set_spreadsheet(get_spreadsheet(config.config_path))
    config.set_availability_spreadsheet(get_availability_spreadsheet(config.config_path))
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

    availability_list = []
    worksheet_titles = []

    for worksheet in google_worksheets:
        logging.info("Fetching all B11 values from " + worksheet.title)
        last_pinged_value = worksheet.get_value('B11')
        worksheet_titles.append(worksheet.title)
        availability_list.append(get_availability(last_pinged_value))
        logging.info("Fetched all B11 values from " + worksheet.title)

    logging.info("All B11 values fetched")

    return worksheet_titles, availability_list


def initialize_availability_sheet():
    logging.info("Initializing availability sheet")
    # Batch write to availability sheet
    # Create a list of worksheet titles
    

def batch_write(spreadsheet, config, servers_availability):
    logging.info("Batch writing")
    worksheets = config.get_worksheets()
    google_worksheets = []

    logging.info("Creating list of worksheets: ")
    for worksheet in worksheets:
        google_worksheets.append(spreadsheet.worksheet_by_title(worksheet))

    logging.info("List of worksheets created")


def pinged_availability(last_pinged_list ):
    logging.info("Checking availability of each server")

    for last_pinged in last_pinged_list:
        print(get_availability(last_pinged))


if __name__ == '__main__':
    # Start timer
    start_time = time.time()

    # Initialize config
    config = Config()
    retrieve_config_values(config)

    # Authorize Google Sheets API
    gc = authorize()



    # Open spreadsheet
    spreadsheet = open_spreadsheet(gc, config)

    # Open availability worksheet
    availability_worksheet = open_availability_worksheet(spreadsheet, config)


    worksheet_titles, availability_list = batch_read(spreadsheet, config)

    # Zip the two lists together
    servers_availability = zip_lists(worksheet_titles, availability_list)
    print(servers_availability)




    print("--- %s seconds ---" % (time.time() - start_time))
