'''
 1) Create a script that allows you to store product ids, names, and prices.
 The code will be very similar to the last example.

 2)	Add error handling code to the code you created in Lab 7-1
 ChangeLog:
    GKim, 2-19-19, Added error handling code

'''
# Data
text_file = None # File Handel
userInput = None # A string which holds user input

# Processing
def WriteProductUserInput(File):
    try:
        print("Type in Product Id, name and price")
        print("Enter 'Exit' to quit!")
        while True:
            userInput = input("Enter Product Id, Name and Price (ex. 1,Chair,55.00): ")
            if userInput.lower() == "exit":
                break
            else:
                File.write(userInput + "\n")
    except Exception as e:
        print("Error: " + str(e))

def ReadFileData(File, Message="Contents of File"):
    try:
        print(Message)
        File.seek(0)
        print(File.read())
    except:
        print("Error: " + str(e))
        
    

# I/O
try:
    text_file = open('C:\_PythonClass\Module07\Module07Demo\Inventory.txt','r+')
    ReadFileData(text_file,"Here is the current data:")
    WriteProductUserInput(File = text_file)
    ReadFileData(text_file,"Here is the data saved:")
except FileNotFoundError as e:
    print("Error: " + str(e) + "\nPlease check file name")
except Exception as e:
    print("Error: " + str(e))
finally:
    if text_file != None:
        text_file.close()