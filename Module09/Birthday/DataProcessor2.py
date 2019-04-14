#------------DataProcessor2.py ---------------#
#Desc:  Classes that read and write data
#Dev:   RRoot 
#Date:  03/05/2019
#ChangeLog:(Who,When,What)
#  GKim, 3-06-19, Re-typed DataProcessor module
#----------------------------------------#

if __name__ == "__main__":
    raise Exception("This file is not meant to be run on its own!!")

class File(object):
    ''' Process data using files '''

    # --Constructor--
    def __init__(self, FileName = "SavedData.txt", TextData = ""):
        # Attributes
        self.FileName = FileName
        self.TextData = TextData

    # --Properties--
    # FileName
    @property
    def FileName(self):
        return self.__FileName

    @FileName.setter
    def FileName(self, Value):
        self.__FileName = Value

    # TextData
    @property
    def TextData(self):
        return self.__TextData

    @TextData.setter
    def TextData(self, Value):
        self.__TextData = Value

    # --Methods--
    def SaveData(self):
        ''' Writes Data '''
        try:
            objFile = open(self.FileName, "a")
            objFile.write(self.TextData + "\n") 
            objFile.close()
        except Exception as e:
            print("Python error message: " + str(e))
        return "Data Saved Successfully"

    def GetData(self):
        ''' Reads Data '''
        try:
            objFile = open(self.FileName, "r")
            self.TextData = objFile.read()
            objFile.close()
        except Exception as e:
            print("Python error message: " + str(e))
        return self.TextData

    def ToString(self):
        ''' Explicitly returns field data '''
        return "{}, {}".format(self.FileName, self.TextData)

    def __str__(self):
        ''' Implicitly returns field data '''
        return self.ToString()

 # --End of Class--

class Database(object):
    ''' Process data using files '''

    # --Constructor--
    def __init__(self, ConnectionString):
        # --Attributes--
        self.ConnectionString = ConnectionString
        raise Exception("this Database class is not ready yet!!")

 # --End of Class