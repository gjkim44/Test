
class Product(object): # Data

    def __init__(self, ProductID, ProductName, ProductPrice):
        self.__ProductID = ProductID
        self.__ProductName = ProductName
        self.__ProductPrice = ProductPrice

    @property
    def ProductID(self): return self.__ProductID
    @ProductID.setter
    def ProductID(self, Value): self.__ProductID = Value

    @property
    def ProductName(self): return self.__ProductName
    @ProductName.setter
    def ProductName(self, Value): self.__ProductName = Value

    @property
    def ProductPrice(self): return self.__ProductPrice
    @ProductPrice.setter
    def ProductPrice(self, Value):
        if Value < 0:
            raise Exception("Price must be greater than zero!")
        else:
            self.__ProductPrice = Value

    def __str__(self):
        return self.ProductID + ',' + self.ProductName + ',' + self.ProductPrice

class FileProcessor(object): # Processing
    #Processing
    
    objE = None
    @staticmethod
    def WriteProductsListToFile(File, ListOfProducts):

        try:
            objF = open(File,'w')
            for prod in ListOfProducts:
                objF.write(str(prod) + "\n")
        except Exception as e:
            raise e
        finally:
            objF.close()

    @staticmethod
    def ReadFileToProductsList(File):
        lstProducts = []
        try:
            objF = open(File, 'r')
            for row in objF:
                lst = row.strip().split(',')
                lstProducts.append(Product(lst[0], lst[1], lst[2]))
        except Exception as e:
            raise e
        finally:
            objF.close()
        return lstProducts


if __name__ == '__main__': # I/O

    strFileName = "Products.txt"
    lstCurrentProductData = []

    def ShowCurrentData(lstData):
        try:
            print("Here is the current data:")
            for prod in lstData:
                print(prod)
        except Exception as e:
            print(e)

    def GetNewData(lstData):
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while (True):
                strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                if (strUserInput.lower() == "exit"):
                    break
                else:
                    lstTemp = str(strUserInput).strip().split(',')
                    objP = Product(lstTemp[0], lstTemp[1], lstTemp[2])
                    lstData.append(objP)
                    ShowCurrentData(lstData)
        except Exception as e:
            print(e)

    def AskToSave(lstData):
        try:
            strAns = input("Save to File (y/n)").strip()
            if strAns.lower() == 'y':
                FileProcessor.WriteProductsListToFile(strFileName, lstData)
        except Exception as e:
            print(e)

    try:
        
        # Load data from File to a List
        lstCurrentProductData = FileProcessor.ReadFileToProductsList(strFileName)
        # Show data in the list
        ShowCurrentData(lstCurrentProductData)
        # Get New Data
        GetNewData(lstCurrentProductData)
        # Show what is Current
        ShowCurrentData(lstCurrentProductData)
        # Ask to Save
        AskToSave(lstCurrentProductData)
    except FileNotFoundError as e:
        print("Error: " + str(e) + "\n Please check the file name")
    except Exception as e:
        print("Error: " + str(e))


