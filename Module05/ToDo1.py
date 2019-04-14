#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   GKim
# Date:  February 6, 2019
# ChangeLog: (Who, When, What)
# RRoot, 11/02/2016, Created starting template
# GKim, 2-06-19, started text file read back to python dictionary
# GKim, 2-07-19, completed working script for Assignment 5
# GKim, 2-08-19, I added other options to give to the user in the form of yes or no
# and to account for choices other than yes or no or 0-4.
# GKim, 2-9-19, edited code for comments and to account for user error, added a conditional
# if the user misspells has numbers, spacing issues when they are trying to remove a task
# GKim, 2-10-19, found a potential user error in choice "2".  When adding a task i gave the user
# an option to make another choice of going to back to menu, but didn't account for "no" and if the user 
# wanted to save data from option and leave.  Found section of global variable, because a "break" does not 
# work in a function that is in a loop.  
# GKim, 2-10-19, choice "3" was not working properly and had to change range(len(lstTable))to range(len(lstTable)-1, -1, -1)
# This made sure I iterated through my list properly 
#-------------------------------------------------#

# This is to slow print statements 
import time
# Global varibale which to be accessable in the program
global active
# Set it to True, as a conditon to keep script active (running)
active = True
# Empty list to write our text file into
lstTable = []
choice = None

# Load data from a text file
text_file = open("C:\_PythonClass\Module05\ToDo1.txt","r")
for line in text_file.readlines():# to read through each line in text file.
    row = line.split(',')
    newDict = {"Task":row[0],"Priority":row[1].replace("\n","")} # .replace("\n","") gets rid of that character
    lstTable.append(newDict) # adds each dictionary to lstTable
text_file.close()

# ------------------------------------------------------------------------ #
# Used functions to make my starting script less bulky
def title():
    title = ["This is the...", "PY", "DO","LIST!!!", "(Also known as the To Do List)"]
    for word in title:
        print("\t\t\t", word,"\n")
        time.sleep(1.25)

# Created function to show data in lstTable
def show_table():
    print("\nUp-to-date Data in table:\n")
    for dict in lstTable:
        print(dict)
    print()   
# Shows the data in raw form to user
def show_data():
    print()
    print("#" * 7, "The current items TO DO are", "#" * 7)
    for dict in lstTable:
        print("{}({})".format(dict["Task"],dict["Priority"]))
        time.sleep(.25)
    print("#" * 43)
    print()
# Shows menu
def menu():
    print ("""
    PYDO Menu of Options
    0) Exit Program
    1) Show To Do List
    2) Add a New Task.
    3) Remove an existing Task.
    4) Save Data to File
    """)
    time.sleep(.75)
# Save data function with exit out of script
def save_data():
    global active 
    save = input("\nWould you like to save data to a text file (y/n)?")
    if save.lower() == "y" or save.lower() == "yes":
        text_file = open("C:\_PythonClass\Module05\ToDo1.txt","w")
        # Iterates through the list
        for dict in lstTable:
            #.get(), gets the value of the key .join (',') joins the 2 values with a comma
            text_file.write(",".join([dict.get('Task'),dict.get('Priority')+ "\n"]))
        text_file.close()
        show_data()
        print("\nYour data has been saved!")
        time.sleep(1)
        active = False
        # Gave the user an out if they selected the wrong choice
    elif save.lower() == "n" or save.lower() == "no":
        active = False
    else:
        print("Not a proper entry, exiting PyDo List")
        active = False
           

# ------------------------------------------------------------------------------ #
# Prints title at start of script   
title()
# Start of Script
# set choice = to None to have a blank starting point for the loop
while choice == None:
# Display a menu of choices to the user
    menu()
    choice = input("\nWhich option would you like to perform? [0 to 4] - ")
    # Exits script
    if choice == "0":
        print("\nYour are leaving the PYDO LIST APP!")
        time.sleep(1)
        break
    
    # Show the current data in the table
    elif choice == "1":
        show_data()
        response = input("Would you like to make another choice (y/n)? ")
        # A quick exit if the data is all the user wanted to see
        if response.lower() == "n" or response.lower() == "no":
            break
        else:
            choice = None
        
    # Add a new Task to the list/Table
    elif choice == "2":
        task1 = input("What is the Task? ")
        priority1 = input("What is the Priority (low|high)? ")
        tpDict = {"Task":task1, "Priority":priority1}
        lstTable.append(tpDict)
        show_data()
        show_table()
        response1 = input("Would you like to make another choice (y/n) ")
        # I gave user an option to enter choice or exit out of script
        if response1.lower() == "n" or response1.lower() == "no":
            # function of save data 
            save_data()
            # If active is False it will break out of loop
            if active == False:
                break
        elif response1.lower() == "y" or response1.lower() == "yes":
            choice = None
        # This line was to account for anything other than yes or no and leads the user back to the main menu
        else:
            print("Not a proper response!  You are being redirected to the main menu")
            time.sleep(1) 
            choice = None   
    #  Remove a Task from the list/Table
    elif choice == "3":
        show_data()
        delete = input("What task would you like to remove? ")
        # ran a for loop to iterate each dictionary in the list.  
        for dict in range(len(lstTable)-1, -1,-1):
            # .get("Task") checks each Task value to delete(user input to remove Task)
            if lstTable[dict].get('Task',None) == delete:
                del lstTable[dict]
                show_data()
                show_table()
                print("The Task of {}, has been removed".format(delete))
                time.sleep(1)
                # Send user right back to main menu
                break
            # Notifies user of error and takes them back to main menu
        else:
            print("\nPlease use proper caps, spacing and no numbers  Else item not found")
            time.sleep(1)
        
    # Save tasks to the ToDo.txt file
    elif choice == "4":
        save = input("\nWould you like to save data to a text file (y/n)?")
        if save.lower() == "y" or save.lower() == "yes":
            text_file = open("C:\_PythonClass\Module05\ToDo1.txt","w")
            # Iterates through the list
            for dict in lstTable:
                #.get(), gets the value of the key .join (',') joins the 2 values with a comma
                text_file.write(",".join([dict.get('Task'),dict.get('Priority')+ "\n"]))
            text_file.close()
            show_data()
            print("\nYour data has been saved!")
            time.sleep(1)
            # Gave the user an out if they selected the wrong choice
        elif save.lower() == "n" or save.lower() == "no":
            backTo = input("\nWould you like to go back to the main menu? ")
            # Added more escape clauses for user error
            if backTo.lower() == "n" or backTo.lower() == "no":
                break
            elif backTo.lower() == "y" or backTo.lower() == "yes":
                choice = None
            else:
                print("That is not a proper response. You are being redirected to the Main Menu!")
                time.sleep(1)
                choice = None 
        choice = None
    # For any number other than 0-4 or even any letter will be displayed this message and divert back to main menu
    else:
        print("\nTHAT IS NOT A PROPER CHOICE!!.  Please choose 0-4: ")
        time.sleep(1.5)
    choice = None
        
# Resetting active to keep script active(running). Active is out of the loop and does not reset 
active = True 
# End of script
print("\nThank you for Stopping By!")
time.sleep(.75)
input("\nPress any key to Exit")        
time.sleep(.75)