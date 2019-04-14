#------------------------------------------#
#Title: Home Inventory Script
#Dev: GKim
#Date: Jan 22, 2019
#ChangeLog: GKim, 1-22-19, Created Script
# GKim, 1-23-19, created HomeInventoryWL to include while loop 
#-------------------------------------------#

#imported time to have a delay on print statements
import time
print("\n\t\t\tThis is the HomeInventory Python Page")
time.sleep(1)
#set choice variable to None to start the while loop
choice = None 
while choice == None:
    #start of script
    print(
        """
        Options for Home Inventory

        0 - exit
        1 - enter information

        """
    )
    #gets input from the user to start the conditional statements
    choice = input("Please enter choice: ")
    #start of condition 1
    if choice == "1":
        #created variables to save data
        item = input("\nPlease enter and Item: ")
        time.sleep(1)
        cost = input("\nPlease enter the Cost of the Item: ")
        time.sleep(1)
        #set inventory variable to make it easy to call on when creating text file
        inventory =(item,cost),
        print("Your data has been saved!", inventory)

        #creating of text file 
        text_file = open('HomeInventoryWL.txt', 'a')
        #writing saved data in string format to text
        text_file.write(str(inventory) + "\n")
        #closing file that was created
        text_file.close()
        #created a variable to ask user if rerun loop or not to enter more information
        response = input("\nWould you like to enter more ( y or n)? ")
        time.sleep(1)
        #condition to set choice back to None to start loop and enter more information or end
        if response.lower() == "y":
            choice = None 
        else:
            choice ="0"
   #exit statement if the user decides not to store any information on the initial choice prompt
    elif choice == "0":
        break
        
print("\nThank you for using the HomeInventory Page!!!!")
time.sleep(1)
input("\n\nPress any key to exit: ")
