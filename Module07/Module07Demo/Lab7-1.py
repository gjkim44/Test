'''
 Create a script that allows you to store product ids, names, and prices.
 The code will be very similar to the last example.

'''
# Data
text_file = None # File Handel
userInput = None # A string which holds user input

# Processing
def WriteProductUserInput(File):
    print("Type in Product Id, name and price")
    print("Enter 'Exit' to quit!")
    while True:
        userInput = input("Enter Product Id, Name and Price (ex. 1,Chair,55.00): ")
        if userInput.lower() == "exit":
            break
        else:
            File.write(userInput + "\n")

def ReadFileData(File, Message="Contents of File"):
    print(Message)
    File.seek(0)
    print(File.read())
    

# I/O
text_file = open('C:\_PythonClass\Module07\Module07Demo\Inventory.txt','r+')

ReadFileData(text_file,"Here is the current data:")

WriteProductUserInput(File = text_file)

ReadFileData(text_file,"Here is the data saved:")

text_file.close()