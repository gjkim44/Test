#------------------------------------------#
#Title: Basic Math Script
#Dev: GKim
#Date: Jan 14, 2019
#ChangeLog: GKim, 1-14-19, Created Script
#-------------------------------------------#

#imported time for looks, on displaying to command prompt when script is run
#time.sleep displays the line with a delay in seconds 
import time
#Beginning of Script  I used a new line, and tab escape characters for display purposes
print("\n\t\t\tWelcome to the Python Math Script!!")
time.sleep(2)

print("\n\t\t\tPlease think of your two FAVORITE numbers")
time.sleep(2)

#input from user, used float just in case the user decided to be tricky with the numbers input
num1 = float(input("\nWhat is your first favorite number: "))
time.sleep(1.5)

num2 = float(input("\nWhat is your second favorite number: "))
time.sleep(1.5)

#math computations of Addition, Subtraction, Multiplicaiton , and Division
add = round((num1 + num2), 3)
sub = round((num1 - num2), 3)
product = round((num1 * num2),3)
quotient = round((num1 / num2), 3) 

#print statements showing the user inputs and the out put for each task , displayed to the user
#also with a time delay for each line from 2-5 seconds
print("\nNow if I ADD", num1,"and", num2,", you would get: ", add,"!!")
time.sleep(2)
print("\nIf I SUBTRACT", num1, "and", num2,", your numbers shrink to: ",sub)
time.sleep(3)
print("\nBUT if I MULTIPLY", num1, "and", num2,", the number drastically increases to: ",
product,"!!")
time.sleep(4)
print("\nIf I DIVIDE", num1, "and", num2, ", the number would be:", quotient)
time.sleep(5)

#end of script
print('\nThank you for helping me with my assignment!')

input("\nPress any key to EXIT")