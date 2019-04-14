class File(object):
    """ Process data using files """

    #--Fields--
    #FileName = name of file
    #TextData = data read from and written to file

    #--Constructor--
    def __init__(self, FileName = "SavedData.txt", TextData = ""):
        #Attributes
        self.FileName = FileName
        self.TextData = TextData

    #--Properties--
    #FileName
    @property
    def FileName(self):
        return self.__FileName

    @FileName.setter
    def FileName(self, Value):
        self.__FileName = Value

    #TextData
    @property
    def TextData(self):
        return self.__TextData

    @TextData.setter
    def TextData(self, Value):
        self.__TextData = Value

    #--Methods--
    def SaveData(self):
        """Writes data"""
        try:
            objFile = open(self.FileName, "a")
            objFile.write(self.TextData)
            objFile.close()
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return "Data Saved"

    def GetData(self):
        """Reads data"""
        try:
            objFile = open(self.FileName, "r")
            self.TextData = objFile.read()
            objFile.close()
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return self.TextData

    def ToString(self):
        """Explictly returns field data"""
        return self.FileName + "," + self.TextData

    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()
#--End of class--