'''
 1) Create a script that allows you to store product ids, names, and prices.
 The code will be very similar to the last example.

 2)	Add error handling code to the code you created in Lab 7-1
 ChangeLog:
    GKim, 2-19-19, Added error handling code

'''


class Product(object):
    '''Base class for Product'''

    # --Constructor--
    def __init__(self, ID, Name, Price):
        # --Attributes--
        self.__ID = ID
        self.__Name = Name
        self.__Price = Price

        # --use in property--
        self.ID = ID
        self.Name = Name
        self.Price = Price

    # -Properties--
    # --ID--
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, Value):
        self.__ID = Value

    # --Name--
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Value):
        self.__Name = Value

    # --Price--
    @property
    def Price(self):
        return self.__Price

    @Price.setter
    def Price(self, Value):
        self._Price = Value

    # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return "{}, {}, {}".format(str(self.ID), str(self.Name), str(self.Price))

    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()


# --END--






# Data

text_file = None  # File Handel
userInput = None  # A string which holds user input

# Processing
def WriteProductUserInput(File):
    try:
        print("Type in Product Id, name and price")
        print("Enter 'Exit' to quit!")
        while True:
            UserInput = input("Enter Product Id, Name and Price (ex. 1,Chair,55.00): ")
            row = UserInput.split(",")
            strID = row[0]
            strName = row[1]
            strPrice = row[2]
            objProd = Product(strID, strName, strPrice)
            # listTable.append(objProd)
            print(objProd.ToString(), ">>>> was added to the list!")
            cont = input("Would you like to enter more (y/n)? ")
            if cont.lower() == "y":
                File.write(objProd.ToString() + "\n")
                continue
            else:
                File.write(objProd.ToString() + "\n")
                break
    except Exception as e:
        print("Error: " + str(e))


def ReadFileData(File, Message="Contents of File"):
    try:
        print(Message)
        File.seek(0)
        print(File.read())
    except:
        print("Error: " + str(e))


# I/O
try:

    text_file = open('C:\_PythonClass\Module07\Module07Demo\Inventory.txt', 'r+')
    ReadFileData(text_file, "Here is the current data:")
    WriteProductUserInput(File=text_file)
    ReadFileData(text_file, "Here is the data saved:")
except FileNotFoundError as e:
    print("Error: " + str(e) + "\nPlease check file name")
except Exception as e:
    print("Error: " + str(e))
finally:
    if text_file != None:
        text_file.close()