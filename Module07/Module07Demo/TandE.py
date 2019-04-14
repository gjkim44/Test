# Display the current data
# The file must be created first before this will work,
#(and a+ does not work here!)
objFile = None
try:
    objFile = open("C:\_PythonClass\Module07\Module07Demo\Inventory.txt", "r+")
    print("Here is the current data:")
    print(objFile.read())

    print("Type in a Customer Id and Name you want to add to the file")
    print("(Enter 'Exit' to quit!)")

    while(True):
        
      strUserInput = input("Enter the Id and Name (ex. 1,Bob Smith): ")
      if(strUserInput.lower() == "exit"): break
      else: objFile.write(strUserInput + "\n")

    print("Here is this data was saved:")
    objFile.seek(0)
    print(objFile.read())
       
except Exception as e:
    print("Python reported the following error: " + str(e))
finally:
    if objFile != None:
        objFile.close()
    print("The program has stopped")
