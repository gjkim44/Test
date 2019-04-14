#------------------------------------------#
#Title: Home Inventory Script
#Dev: GKim
#Date: Jan 29, 2019
#ChangeLog: GKim, 1-22-19, Created Script
# GKim, 1-23-19, created HomeInventoryWL to include while loop 
# GKim, 1-29-19, reformatted HomeInventory WL to incorporate tuple and give the user
# an option to save the information inputed or not.  Created a new variable to hold
# the 2-dimensional tuple and moved the creation of the text file code to a different
# section and set new conditions to ask the user if they would like to save or not.
# GKim, 2-4-19, created a for loop to unpack 2 dimensional tuple
#-------------------------------------------#

# imported time to have a delay on print statements
import time
def menu():

    print(
        """
        Options for Home Inventory

        0 - exit 
        1 - enter information

        """
    )
print("\n\t\t\tThis is the HomeInventory Python Page")
time.sleep(1)
# variable to hold tuples from user
tuple_inventory = ()
# set choice variable to None to start the while loop
choice = None 
while choice == None:
    # start of script
    menu()
    # gets input from the user to start the conditional statements
    choice = input("Please enter choice: ")
    if choice == "0":
        break
    
    # start of condition 1
    elif choice == "1":
        item = input("\nPlease enter and Item: ")
        time.sleep(1)
        cost = input("\nPlease enter the Cost of the Item: ")
        time.sleep(1)
        # set inventory variable to make it easy to call on when creating text file adding coma to make it a tuple
        # inventory =(item,cost),
        # concatenating tuple to add more items to it
        tuple_inventory += (item +", "+ cost),
        # created a variable to ask user if rerun loop or not to enter more information
        response = input("\nWould you like to enter more ( y or n)? ")
        time.sleep(1)
        if response.lower() == "y" or response.lower() == "yes":
            choice = None
        # giving the user the option to save data or not upon exiting     
        elif response.lower() == "n" or response.lower() == "no":
            print("You are exiting Home Inventory\n")
            save_info = input("\nWould you like to save your information and write it to a text file (y or n)? ")
            if save_info.lower() == "y" or save_info.lower() =="yes":
                # creating of text file 
                text_file = open('HomeInventory2.txt', 'a') 
                # writing saved data in string format to text
                text_file.write("ITEM:  COST:" + "\n")
                # Using a for loop to unpack 2 dimensional tuple
                for row in tuple_inventory:
                    text_file.write(row + "\n")
                # closing file that was created
                text_file.close()
                print("Your data has been saved!", tuple_inventory)
                break
                       
            else:
                break
        else:
            print("That is not a proper response.  You are leaving HomeInventory")
            break
    else:
        choice = None
       

    
print("\nThank you for using the HomeInventory Page!!!!")
time.sleep(1)
input("\n\nPress any key to exit: ")
