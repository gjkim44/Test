
class Product:

    def __init__(self, ProductID, ProductName, ProductPrice):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.ProductPrice = ProductPrice


    def __str__(self):
        return self.ProductID + ',' + self.ProductName + ',' + self.ProductPrice


class dataprocessing:

    #Data
    objFile = None #File Handle
    strUserInput = None #A string which holds user input

    #Processing
    @staticmethod
    def WriteProductUserInput(File):
      try:
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)")
        while(True):
          strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
          if(strUserInput.lower() == "exit"): break
          else: File.write(strUserInput + "\n")
      except Exception as e:
        print("Error: " + str(e))

    @staticmethod
    def ReadAllFileData(File, Message="Contents of File"):
      try:
        print(Message)
        File.seek(0)
        print(File.read())
        File.seek(0)
        for row in File:
            lst = row.strip().split(',')
            p = Product(lst[0],lst[1],lst[2])
            print(p)

      except Exception as e:
        print("Error: " + str(e))



#I/O
try:
  dataprocessing.objFile = open("Products.txt", "r+")
  dataprocessing.ReadAllFileData(dataprocessing.objFile, "Here is the current data:")
  dataprocessing.WriteProductUserInput(dataprocessing.objFile)
  dataprocessing.ReadAllFileData(dataprocessing.objFile, "Here is this data was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(dataprocessing.objFile != None):dataprocessing.objFile.close()
