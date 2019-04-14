#-------------------------------------------------#
# Title: Classes and Objects
# Dev: GKim 
# Date: February 27, 2019
# ChangeLog: (Who, When, What)
#   GKim, 2-27-19, Created Script
#   GKim, 3-01-19, Created product class to store id, name, price
#   GKim, 3-03-19, Created Textfile class to write data to Data text 
# and child class of Readme of TextFile to read data and.   
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

#Data
#Processing
class TextFile(object):
    '''Base Class for Text file'''
    # --Constructor--
    def __init__(self, File):
        self.__File = File

    # --Properties--
    # --File--
    @property
    def File(self):
        return self.__File

    @File.setter
    def File(self, Value):
        self.__File = Value

    # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return "{}".format(str(self.File))

    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
    # --Writes data to file--
    def WriteProductInput(self):
        try:
            print("\nType in a Product Id, Name, and Price you want to add to the file")
            while(True):
                strUserInput = input("\nEnter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                # Extracted data from user input into a list format to use index
                row = strUserInput.split(",")
                strID = row[0]
                strName = row[1]
                strPrice = row[2]
                # variable to hold data from Class Product
                objProd = Product(strID,strName,strPrice)
                # listTable.append(objProd)
                # Display the string format of the data from user in the Class
                print(objProd.ToString(),">>>> was added to the list!")
                # I kept recieving an error message with the original code using exit to break.  There was a 
                # list index error out of range.  It was using exit to store as strID and nothing else followed
                # giving me that error.  I had to set a condition to ask if the user would like to enter more. in
                # continuing with the loop and breaking out of the loop I had to write to file in both statements 
                # to save data.  If you entered more than 1 entries, it would not save the last piece of data if you wanted
                # exit. 
                cont = input("Would you like to enter more (yes/no)? ")
                if cont.lower() == "yes" or cont.lower() == "y":
                    self.File.write(objProd.ToString() + "\n")
                    continue
                else:
                    self.File.write(objProd.ToString() + "\n") 
                    break
                
        except Exception as e:
            print("Error!: " + str(e))
    
    # ---End of class---


    # --Beginning of Child Class--
class ReadMe(TextFile):
    '''Child to TextFile'''
    # --Constructor--
    def __init__(self, File, Message=" "):
        # calls on the parent (inheritance)
        super(ReadMe,self).__init__(File)
        self.__Message = Message
   
    #--Properties
    @property 
    def Message(self):
        return self.__Message

    @Message.setter
    def Message(self, Value):
        self.__Message = Value


    # ---Methods---
    def ToString(self):
        '''Explicitly returns field data'''
        return "{}, {}".format(str(self.File),str(self.Message))

    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
    # --Reads data--
    def ReadData(self):
        try:
            print(self.Message)
            self.File.seek(0)
            print(self.File.read())
        except Exception as e:
            print("Error: " + str(e))
    # ---End of class---





#I/O
try:
    # variables in try block so they are not global
    objFile = None 
    strUserInput = None 
    listTable =[]
    objFile = open("C:\_PythonClass\Module08\Assignment08\Products.txt", "r+")
    # creating a new object to read data
    readData = ReadMe(objFile, "\n****Current Data****")
    readData.ReadData()
    # created an object to write product info
    writeProd = TextFile(objFile)
    writeProd.WriteProductInput()
    # created a second object to read saved data
    readData2 = ReadMe(objFile, "\n*****Saved Data*****")
    readData2.ReadData()
except FileNotFoundError as e:
    print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
    if(objFile != None):
        objFile.close()
