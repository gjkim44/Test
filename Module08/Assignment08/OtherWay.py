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
    def __init__(self, Name):
        # --Attributes--
        self.__Name = Name

    # --Name--
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Value):
        self.__Name = Value

    # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return "{}".format(str(self.Name))
    
    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
    # --END--    


class IdPrice(Product):
    '''Class for ID and Price'''

    # --Constructor--
    def __init__(self, ID, Name, Price):
        self.__ID = ID
        self.Name = Name
        # super(IdPrice, self).__init__(Name)
        self.__Price = Price

    # --Properties--
    # --ID--
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, Value):
        self.__ID = Value

    # --Price--
    @property
    def Price(self):
        return self.__Price

    @Price.setter
    def Price(self, Value):
        self.__Price = Value
    
    # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return "{}, {}, {}".format(str(self.ID),str(self.Name),str(self.Price))



#Data
#Processing
def WriteProductUserInput(File):
    lstTable = []
    try:
        print("\nType in a Product Id, Name, and Price you want to add to the file")
        while(True):
            strUserInput = input("\nEnter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
            row = strUserInput.split(",")
            strID = row[0]
            strName = row[1]
            strPrice = row[2]
            objProd = IdPrice(strID,strName,strPrice)
            lstTable.append(objProd)
            print(objProd.ToString(),">>>> was added to the list!")
            cont = input("Would you like to enter more (yes/no)? ")
            if cont.lower() == "yes" or cont.lower() == "y":
                File.write(objProd.ToString() + "\n")
                continue
            else:
                File.write(objProd.ToString() + "\n") 
                break
               
    except Exception as e:
        print("Error!: " + str(e))

def ReadAllFileData(File, Message="Contents of File"):
    try:
        print(Message)
        File.seek(0)
        print(File.read())
    except Exception as e:
        print("Error: " + str(e))


    # lstTable = []
    
    # for line in objFile.readlines():
    #     lstData = line.split(",") # readline() reads a line of the data into 2 elements
    #     lstTable.append(lstData.replace("\n",""))
    # objFile.close()
    # return lstTable








#I/O
try:
    objFile = None #File Handle
    strUserInput = None #A string which holds user input
    objFile = open("C:\_PythonClass\Module08\Assignment08\Products.txt", "r+")
    loadTable = 
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
