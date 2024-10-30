import logging
from datetime import date
import threading
logger = logging.getLogger(__name__)

class dataMaintainer:
    def real_time_read_logs(self):
        handler = logging.handlers.WatchedFileHandler(filename)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        while True:
            time.sleep(1)  # Check for new log entries every second

    loggingThread = threading.Thread(target = real_time_read_logs, args = ())

    def __generateLogFile(self, fileName:str):
        logging.basicConfig(filename = date.today().strftime("%Y-%m-%d_") + fileName, level = logging.INFO)
        return

    def __init__(self, fileName):
        self.__generateLogFile(fileName)
        self.loggingThread.start()
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
    def __del__(self):  # body of destructor
        self.loggingThread.join()
        logging.info("Closed Data Maintainer")