#------------------------------------------#
#Title: Home Inventory Script
#Dev: GKim
#Date: Jan 22, 2019
#ChangeLog: GKim, 1-22-19, Created Script
#-------------------------------------------#
#imported time to have a delay on print statements
import time

#start of script
print("\n\t\t\tThis is the HomeInventory Python Page")
time.sleep(1)
#created variables to save data
item = input("\nPlease enter and Item: ")
time.sleep(1)
cost = input("\nPlease enter the Cost of the Item: ")
time.sleep(1)

#set inventory variable to make it easy to call on when creating text file
inventory =(item,cost)
print("Your data has been saved!", inventory)

#creating of text file 
text_file = open('HomeInventory.txt', 'a')
#writing saved data in string format to text 
text_file.write(str(inventory)+ "\n")
#closing file that was created
text_file.close()