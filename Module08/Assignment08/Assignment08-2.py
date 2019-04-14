#-------------------------------------------------#
# Title: Classes and Objects
# Dev: GKim 
# Date: February 27, 2019
# ChangeLog: (Who, When, What)
#   GKim, 2-27-19, Created Script
#   
#-------------------------------------------------#

class ProductInfo(object):
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
    # @staticmethod
    def ProductInput(self, ID = "", Name = "", Price = ""):
        try:
            print("\nType in a Product Id, Name, and Price you want to add to the file")
            while(True):
                strUserInput = input("\nEnter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                row = strUserInput.split(",")
                strID = row[0]
                strName = row[1]
                strPrice = row[2]
                objProd = ProductInfo(strID,strName,strPrice)
                listTable.append(objProd)
                print(objProd.ToString(),">>>> was added to the list!")
                cont = input("Would you like to enter more (yes/no)? ")
                if cont.lower() == "no" or cont.lower() == "n":
                    break
        except Exception as e:
            print("Error!: " + str(e))


class DataFile(object):
    '''Base class for Data file'''
    # --Constructor--
    def __init__(self, File, myTable):
        # --Attribute--
        self.__File = File
        self.__myTable = myTable
        
    # --Properties--
    # File
    @property
    def File(self):
        return self.__File

    @File.setter
    def File(self, Value):
        self.__File = Value

    @property
    def myTable(self):
        return self.__myTable

    @myTable.setter
    def myTable(self, Value):
        self.__myTable = Value

    def ToString(self):
        return str(self.File)

    def __str__(self):
        return self.ToString()
    
        
    # --Method--
    # @staticmethod
    def LoadData(self):
        text_file = open(self.ToString,"r+")
        for line in text_file.readlines():# to read through each line in text file.
            row = line.split(',')
            newList = [row[0],row[1],row[2].replace("\n","")]
            self.myTable.append(newList) # adds each dictionary to lstTable
        text_file.close()
        return self.myTable

    # @staticmethod
    def ReadData(self):
        print("#" * 7, "The Current Products", "#" * 7)
        for row in self.myTable:
            print("{},{},{}".format(row[0],row[1],row[2]))

    def SaveData(self):
        strAnswer = input("Save Data to file (y/n)")
        myFile = open(self.ToString(), "r+")
        if strAnswer.lower() == "y":
            strAllText = ""
            for item in listTable:
                strData = item + '\n'
                myFile.write(strData)
                strAllText += strData
            myFile.close()
            print("The following data was saved to a file: \n",strAllText)
        else:
            print("Data was not saved!")
    




#I/O
listTable = []
try:
    objFile ="C:\_PythonClass\Module08\Assignment08\Products.txt"
    lData = DataFile(objFile, listTable)
    listTable = lData.LoadData()
    DataFile.ReadData(listTable)
    ProductInfo.ProductInput("", "", "")
    dataF = DataFile(objFile,listTable)
    dataF.SaveData()
except FileNotFoundError as e:
    print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
