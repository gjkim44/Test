if __name__ == "__main__":
    import DataProcessor
else:
    raise Exception("This file was not created to be imported ")

objP = DataProcessor.File()
objP.FileName = "Test.txt"
objP.TextData = "This is a test"
strMessage = objP.SaveData()
print(strMessage)