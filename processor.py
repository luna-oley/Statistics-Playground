from dataHandling.handling import *
from dataInput.input import *
from dataStorage.storage import *

# Defining main function
def main():
    print("Hello World")

    storage = dataMaintainer("debugLog.log")
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

