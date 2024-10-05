from dataHandling.handling import *
from dataInput.input import *
from dataStorage.storage import *

# Defining main function
def main():
    print("Hello World")

    storage = dataMaintainer()
    handler = dataHandler()
    reciever = dataReceiver()

    handler.print_handling()
    reciever.print_input()
q    storage.print_storage()

# Using the special variable
# __name__
if __name__=="__main__":
    main()

