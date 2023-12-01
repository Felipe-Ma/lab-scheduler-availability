from datetime import datetime
import os
import yaml


class Config:
    def __init__(self, current_directory=None, config_path=None, credential_path=None,
                 spreadsheet=None, worksheets=None):
        self.current_directory = current_directory
        self.config_path = config_path
        self.credential_path = credential_path
        self.spreadsheet = spreadsheet
        self.worksheets = worksheets

    def set_current_directory(self, current_directory):
        self.current_directory = current_directory

    def set_config_path(self, config_path):
        self.config_path = config_path

    def set_credential_path(self, credential_path):
        self.credential_path = credential_path

    def set_spreadsheet(self, spreadsheet):
        self.spreadsheet = spreadsheet

    def set_worksheets(self, worksheets):
        self.worksheets = worksheets

    # Print all config values
    def __call__(self):
        print("Current Directory: " + str(self.current_directory))
        print("Config Path: " + str(self.config_path))
        print("Credential Path: " + str(self.credential_path))
        print("Spreadsheet: " + str(self.spreadsheet))
        print("Worksheet: " + str(self.worksheets))


def get_current_directory():
    current_directory = "Unknown"
    try:
        current_directory = os.path.dirname(os.path.realpath(__file__))
    except Exception as e:
        print(str(e) + "Error getting current directory")
    return current_directory


def get_config_path(main_directory):
    config_path = "Unknown"
    try:
        config_path = os.path.join(main_directory, 'config.yaml')
    except Exception as e:
        print(str(e) + "Error getting config path!")
    return config_path


# Get Path of Credentials File
def get_credential_path(config_path):
    credentials_path = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            credential_name = config['credentialsName']
            # Extract the directory from the config_path
            config_directory = os.path.dirname(config_path)
            # Join the directory path with the credential file name
            credentials_path = os.path.join(config_directory, credential_name)
    except Exception as e:
        print(str(e) + "Error getting credentials path!")
    return credentials_path


def get_spreadsheet(config_path):
    spreadsheet = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            spreadsheet = config['spreadsheet']
    except Exception as e:
        print(str(e) + "Error getting spreadsheet name!")
    return spreadsheet

def get_worksheets(config_path):
    worksheets = "Unknown"
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
            worksheets = config['worksheets']
    except Exception as e:
        print(str(e) + "Error getting worksheet names!")
    return worksheets

def get_time():
    current_datetime = datetime.now()
    print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")
