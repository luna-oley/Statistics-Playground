import logging
from datetime import date
logger = logging.getLogger(__name__)

class dataMaintainer:
    def __generateLogFile(self, fileName:str):
        logging.basicConfig(filename = date.today().strftime("%Y-%m-%d_") + fileName, level = logging.INFO)
        return

    def __init__(self, fileName):
        self.__generateLogFile(fileName)
        return

    def print_storage(self):
        print("Hello from storage")
        return

    def write_to_log_file(self, message):
        logging.info(message)
        return
    def read_log_file_to_console(self, fileName):
        with open(fileName, 'r') as logFile:
            for line in logFile:
                print(line.strip())
        return
