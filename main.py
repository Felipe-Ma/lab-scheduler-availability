import os.path

import pygsheets
import time
import logging
from functions import *

#get_time()
#start_time = time.time()
# Log in terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')





#print(gc.spreadsheet_ids())
#print(gc.spreadsheet_titles())

#logging.info("Opening all spreadsheets")
#wks = gc.open_all()


#spreadsheet = wks[1]

# logging.info("Opening worksheet 1")
#print(spreadsheet)

#logging.info("Return worksheets as csv")
#spreadsheet.export(path=os.path.dirname(os.path.realpath(__file__)), filename="worksheets.csv")
#print(spreadsheets.worksheets())
#worksheet1 = spreadsheet[0]

#worksheet1.link()
#worksheet1.get_all_values()

#worksheet1 = spreadsheets.worksheet("Yoda 1")
#print(worksheet1)



#sh.link()

# Create Spreadsheet

#sh = gc.open("Server Dashboard")
#sh = pygsheets.Spreadsheet(sh)
#print(sh.updated())

#print(sh.updated())
#wks = sh.worksheet_by_title("Yoda")
#print(wks.updated())

def authorize():
    logging.info("Authorizing Google Sheets API")
    gc = pygsheets.authorize(service_file="testing.json")

    return gc

    #logging.info("Opening spreadsheet 1")
    #spreadsheet = gc.open("Server Dashboard")


def retrieve_config_values(config):
    config()
    logging.info("Retrieving config values")
    config.set_current_directory(get_current_directory())
    config.set_config_path(get_config_path(config.current_directory))
    config.set_credential_path(get_credential_path(config.config_path))
    config.set_spreadsheet(get_spreadsheet(config.config_path))
    config.set_worksheets(get_worksheets(config.config_path))
    config()

if __name__ == '__main__':
    start_time = time.time()

    config = Config()
    retrieve_config_values(config)
    #gc = authorize()

    print("--- %s seconds ---" % (time.time() - start_time))
