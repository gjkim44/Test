#-------------------------------------------------#
# Title: Classes and Objects
# Dev: GKim 
# Date: February 27, 2019
# ChangeLog: (Who, When, What)
#   GKim, 2-27-19, Created Script
#   
#-------------------------------------------------#

class Product(object):
    '''Base class for Product'''

    # --Constructor--
    def __init__(self, ID, Name, Price):
        # --Attributes--
        self.__ID = ID 
        self.__Name = Name
        self.__Price = Price

        # --use in property--
        # self.ID = ID
        # self.Name = Name
        # self.Price = Price
    
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
        return "{}, {}, {}".format(str(self.ID),str(self.Name),str(self.Price))
    
    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
  # --END--    

# -----------------Functions------------------- #
# ------------Input/output
def UserInput():
    print("\nType in a Product Id, Name, and Price you want to add to the file")
    strUserInput = input("\nEnter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
    return strUserInput

def InputMore():
    cont = input("Would you like to enter more (yes/no)? ")
    return cont



# ---------------Data Processing--------------#
def InsertInfo(strUserInput):
    row = strUserInput.split(",")
    strID = row[0]
    strName = row[1]
    strPrice = row[2]
    objProd = Product(strID,strName,strPrice)
    print(objProd.ToString(),">>>> was added to the list!")
    return objProd


def WriteToFile(File, objProd, cont):
    if cont.lower() == "yes" or cont.lower() == "y":
        File.write(objProd.ToString() + "\n")
        continue
    else:
        File.write(objProd.ToString() + "\n") 
        break


def WriteProductUserInput(File):
    
        while(True):
            # listTable.append(objProd)



#Data
#Processing
class TextFile(object):
    '''Base Class for Text file'''

    def __init__(self, File, Message=" "):
        self.__File = File
        self.__Message = Message 
    
    @property
    def File(self):
        return self.__File

    @File.setter
    def File(self, Value):
        self.__File = Value

    @property 
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, Value):
        self.__Message = Value


    # ---Methods---
    def ToString(self):
        return "{}, {}".format(str(self.File),str(self.Message))

    def ReadData(self):
        try:
            print(Message)
            File.seek(0)
            print(File.read())
        except Exception as e:
            print("Error: " + str(e))

#I/O
try:
    objFile = None #File Handle
    strUserInput = None #A string which holds user input
    listTable =[]
    objFile = open("C:\_PythonClass\Module08\Assignment08\Products.txt", "r+")
    ReadAllFileData(objFile, "\n****Current Data****")
    WriteProductUserInput(objFile)
    ReadAllFileData(objFile, "\n*****Saved Data*****")
except FileNotFoundError as e:
    print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
    if(objFile != None):
        objFile.close()
