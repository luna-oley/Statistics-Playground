from dataHandling.handling import *
from dataInput.input import *
from dataStorage.storage import *
import sys

def handle_arguments():
    if len(sys.argv)>=2:
        print(sys.argv[1])


# Defining main function
def main():
    handle_arguments()
    storage = dataMaintainer("debugLog.log")
    print("123")
    handler = dataHandler()
    reciever = dataReceiver()

    handler.print_handling()
    reciever.print_input()
    storage.print_storage()

    storage.write_to_log_file("I am a bill")
    storage.read_log_file_to_console("2024-10-12_debugLog.log")

# Using the special variable
# __name__
if __name__=="__main__":
    main()

