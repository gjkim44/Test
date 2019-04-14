#-------------------------------------------------#
# Title: Try and Except Files
# Dev: GKim 
# Date: February 19, 2019
# ChangeLog: (Who, When, What)
#   GKim, 2-19-19, Created Script
#   GKim, 2-20-19, Added pickling and unpickling data.  Added functions
# and try and except blocks.  Was able to load pickle list and show entire
# list in binary file via a while loop.
#   GKim, 2-21-19, Added custom error class to draw message for leaving name input blank
#-------------------------------------------------#
# Imported pickle function to pickle data
import pickle 

listC = [] # Empty list to unload pickledata into
objFile = "C:\_PythonClass\Module07\Assignment07\Customers.dat"
text_file = None

# please use this if using in command prompt or a mac
# objFile = "Customers.dat" 


# Error classes to draw on custom exception
class Error(Exception):
    '''Base class for other exceptions'''
    pass
# Custom error message for leaving name input blank
class NoInputError(Error):
    '''Raised when there is no input from user'''
    pass


# Presentation / data functions
def readData(FileName):
    # Opens Binary file
    text_file = open(FileName, "rb")
    # Run a while loop to unpickle data from Binary file
    while True:
        try:
            listC.append(pickle.load(text_file)) # append unpickle data into empty list
        except EOFError: # Unpickle data will unload until it reaches end of file then breaks
            break
    text_file.close()
    return listC

# Shows Current pickled data in raw form
def showData(lstTable):
    print("\n****Current Customer List****")
    for list in lstTable:
        print("{}: {}".format(list[0],list[1]))

# Writes data to Binary file via Pickle
def writeData(FileName):
    text_file = open("C:\_PythonClass\Module07\Assignment07\Customers.dat", "ab")
    custId = int(input("\nEnter an Id: "))
    custName = str(input("\nEnter a Name: "))
    # Created a conditional to raise a custom error if input string is left blank
    if custName == "": 
        raise NoInputError
    lstCustomer = [custId, custName]
    # Pickled data put into Binary file
    pickle.dump(lstCustomer, text_file)
    print("\n{} was added to the list at Id: {}.".format(custName,custId))
    
    
 
        
# I/O
try:
    listC = readData(FileName = objFile)
    showData(lstTable = listC)
    writeData(FileName = objFile)

    # Error raised if file name or path is incorrect
except FileNotFoundError:
    print("Please check file name or path")

    # Error raised for blank input on name
except NoInputError:
    print("You must enter a name, do not leave it blank")

    # Exception to raise error for letters put into Id section of input
except Exception as e:
        print("You must enter a NUMBER")
        print("Python error message: " + str(e))
    # If the code has passed and messages displayed if text_file has a path it will close the file
finally:
    if text_file != None:
        text_file.close()
   


