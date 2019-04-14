import DataProcessor


objP = DataProcessor.File()
objP.FileName = "Test.txt"
objP.TextData = "This is a test"
strMessage = objP.SaveData()
print(strMessage)
