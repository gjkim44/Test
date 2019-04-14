#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  Sept 16, 2017
# ChangeLog: (Who, When, What)
#   RRoot, 09/16/2017, Created Script
#   GKim, 2-13-2019, added class PresentationFunctions and made functions for 
#   reading text file and showing raw data, add data, remove data, save file
#   GKim, 2-14-2019, Added Function document header and description to each function
#-------------------------------------------------#


objFileName = "Todo2.txt"
# objFileName = "C:\_PythonClass\Module06\Assignment06\Todo2.txt" # used when run in virtual environment
strData = ""
dicRow = {}
lstTable = []


class PresentationFunctions:
    ''' Desc: A section of functions with in a class 
        Functions: ReadFileData()
                   menu()
                   RawData()
                   AddData()
                   RemoveData()
                   SaveData()
    '''


    @staticmethod
    def ReadFileData(FileName):
        ''' Desc: This Function reads from a text file and writes it to a dictionary then appends it in a list 
            objFile: Text file variable for the text file to be opened
            open: Opens the file at the directory listed in FileName
            FileName: Variable where input of directory needs to be 
            line: Line in the text file
            lstData: Varaible to save line from text file into a list form
            dicRow: Dictionary variable to store the data from lstData into a dictionary
            lstTable: Main empty variable to store dictionary from text file upon program opening
            .close(): Closes the text file
            return: Returns lstTable after text file is done reading/writing to python 
        '''

        objFile = open(FileName, "r")
        for line in objFile:
            lstData = line.split(",") # readline() reads a line of the data into 2 elements
            dicRow = {"Task":lstData[0].strip(), "Priority":lstData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        return lstTable

    @staticmethod
    def menu():
        ''' Desc: This Function just prints the menu.
            x: Variable to return print() out of function
        '''
        print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
        strChoice = str(input("\nWhich option would you like to perform? [1 to 4] - \n"))
        return strChoice

    @staticmethod
    def RawData(myTable):
        ''' Desc: This Functions shows the data in a presentable form to the user 
            row: Variable for for loop to go through each row of myTable
            myTable: List where informtion is gathered from 
            print(): Prints information with in parentheses
        '''

        print("******* The current items ToDo are: *******")
        for row in myTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    @staticmethod
    def AddData(myTable):
        '''Desc: This Function adds a task(data) inputed by the user and adds it to the list 
           strTask: Input gathered from user as data task
           strPriority: Input gather from user for data priority
           dicRow: Dictionary variable to store data from user
           .append(): To put data from dictionary in lstTable 
           print(): Prints information with in parentheses
           myTable: List where informtion is gathered from
           PresentationFunctions.RawData(myTable): Class and function called to show raw data
           return: Returns function and breaks out of loop.(can not use break or continue with in a function)
        '''

        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task":strTask,"Priority":strPriority}
        myTable.append(dicRow)
        print("Current Data in table:")
        for dicRow in myTable:
            print(dicRow)
        PresentationFunctions.RawData(myTable)
        return

    @staticmethod
    def RemoveData(myTable):
        ''' Desc: This Function removes data from the list 
            strKeyToRemove: Data to remove from lstTable, from input of user
            blnItemRemoved: Boolean variable to use with in while loop for use in conditionals
            intRowNumber: Starts at index 0, used in while loop condition 
            while(): While loop, runs script as long as intRowNumber is less than the length of the list table
            if(), else: Conditions to compare varibales to run certain parts of script
            del: Deletes data from list 
            PresentationFunctions.RawData(myTable): Class and function called to show raw data
            return: Returns function and breaks out of loop.(can not use break or continue with in a function)
        '''

                #5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False #Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(myTable)):
            if(strKeyToRemove == str(list(dict(myTable[intRowNumber]).values())[0])): #the values function creates a list!
                del myTable[intRowNumber]
                blnItemRemoved = True
            #end if
            intRowNumber += 1
        #end for loop
        #5b-Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #5c Show the current items in the table
        PresentationFunctions.RawData(myTable)
        return

    @staticmethod
    def SaveData(FileName,myTable):
        ''' Desc: This Function saves the current data 
            PresentationFunctions.RawData(myTable): Class and function called to show raw data
            if(), else: Conditions to compare varibales to run certain parts of script
            str(input): Gather input from user
            .strip(): Get rid of quotes from string
            .lower(): lower cases input from user
            objFile: Text file variable for the text file to be opened
            open: Opens the file at the directory listed in FileName
            FileName: Variable where input of directory needs to be
            myTable: Variable where we get our list from 
            dicRow: Variable to iterated through myTable row 
            .write(): Writes to a line in the text file
            .close(): Closes the text file
            return: Returns to break out of loop
        '''

        #5a Show the current items in the table
        PresentationFunctions.RawData(myTable)
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(FileName, "w")
            for dicRow in myTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        return
    


# Loads text file data to lstTable
lstTable = PresentationFunctions.ReadFileData(FileName = objFileName)
#Body of Script
while(True):
    # Display a menu of choices to the user
    
    strChoice = PresentationFunctions.menu()
      
    # Show the current items in the table
    if (strChoice.strip() == '1'):
        PresentationFunctions.RawData(myTable = lstTable)
        
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        PresentationFunctions.AddData(myTable = lstTable)
        
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        PresentationFunctions.RemoveData(myTable = lstTable)
        
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        PresentationFunctions.SaveData(FileName = objFileName,myTable = lstTable)
       
    elif (strChoice == '5'):
        break #and Exit the program

