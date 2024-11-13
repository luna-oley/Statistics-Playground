from dataHandling.handling import *
from dataInput.input import *
from dataStorage.storage import *
import sys

def handle_arguments():
    if len(sys.argv)>=2:
        print(sys.argv[1])


# Defining main function
def main():
    storage = dataMaintainer("debugLog.log")
    handle_arguments()
    handler = dataHandler()
    reciever = dataReceiver()

    storage.read_log_file_to_console("2024-10-12_debugLog.log")

# Using the special variable
# __name__
if __name__=="__main__":
    main()

