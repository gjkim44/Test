#-------------------------------------------------#
# Title: CustomerApp
# Dev:   RRoot
# Date:  03/05/2019
# Desc: This application mges Customer data
# CheLog: (Who, When, What)
#  GKim, 3-06-19, Re-typed MyApp and changed to customer.  Added Birthday condition to 
# print messBirthday and break out of loop 
#  GKim, 3-10-19, added input year, month, day to user input to capture data for 
# datetime function to calculate age.  Added condition to check for age verification
# and break out of loop if true.  Moved Process input in else of condition.
#-------------------------------------------------#

if __name__ == "__main__":
    import DataProcessor2, Customers2, datetime
else:
    raise Exception("This file wasn't created to be imported")

#-- Data --# 
# Variable constants
objCust = None # Customer objCust
intId = 0 # CustomerId
gIntLastId = 0 # Records the last CustomerId used in the client
strFirstName = "" # Customer's First name
strLastName = "" # Customer's Last name
intBirthday = None # Customer's Birthday
strAddress = "" # Customer's Address
strPhoneNumber = "" # Customer's Phone Number
strEmail = "" # Customer's Email
strInput = "" # temporary user input

# -- Processing --#
# perform tasks
def ProcessNewCustomerData(Id, FirstName, LastName, Birthday, Address, PhoneNumber, Email):
    try:
        # Create Customer objCust
        objCust = Customers2.Customer()
        objCust.Id = Id
        objCust.FirstName = FirstName
        objCust.LastName = LastName
        objCust.Birthday = Birthday
        objCust.Address = Address
        objCust.PhoneNumber = PhoneNumber
        objCust.Email = Email
        Customers2.CustomerList.AddCustomer(objCust)
    except Exception as e:
        print(e)

def SaveDataToFile():
    try:
        objF = DataProcessor2.File()
        # objF.FileName = "C:\_PythonClass\Module09\Assignment09\CustomerData2.txt"
        objF.FileName = "CustomerData2.txt"
        objF.TextData = Customers2.CustomerList.ToString()
        print("Data was entered correctly with no errors.")
        objF.SaveData()
    except Exception as e:
        print(e)



# -- Presentation (I/O) --#
# __main__
try:        
    # User input
    strUserInput = ""
    TFAge = None
    while(True): 
        strUserInput = input("Would you like to add Customer data? (y/n) ")
        if strUserInput.lower() == "y" or  strUserInput.lower() == "yes":
            # Customer Id from the User
            intId = int(input("Enter Customer Id (Last Id was {}): ".format(str(gIntLastId))))
            gIntLastId = intId
            # Customer FirstName from the User
            strFirstName = input("Enter Customer First Name: ")
            # Customer LastName from the User
            strLastName = input("Enter Customer Last Name: ")
            # Customer Birthday from user
            year = int(input("Enter Customer Birth year: "))
            month = int(input("Enter Birth month: "))
            day = int(input("Enter Brith day: "))
            intBirthday = datetime.date(year, month, day)
            # Customer Address from User
            print("\nCustomer Address ex: 1111 Main St. Seattle, WA 98108")
            strAddress = input("Enter Customer Address: ")
            # Customer Phone Number 
            print("\nCustomer Phone Number ex: 555 555 5555")
            strPhoneNumber = input("Enter Customer Phone Number: ")
            # Customer Email
            print("\nCustomer Email ex: JaneDoe@hotmail.com")
            strEmail = input("Enter Customer Email: ")
            # created test object to run age verification
            test = Customers2.Customer(intId, strFirstName, strLastName, intBirthday, strAddress, strPhoneNumber, strEmail)
            TFAge = test.ageVerification() # age verification results
            if TFAge == False:
                print("\nPlease restart application without previous Customer")
                break
                # Continues if age meets requirements
            else:
                #Process input
                ProcessNewCustomerData(intId, strFirstName, strLastName, intBirthday, strAddress, strPhoneNumber, strEmail)
                #send program output
                print("Here is the Current Data: ")
                print("------------------------")
                print(Customers2.CustomerList.ToString())

                #user input
                strInput = input("Would you like to save this data to file(y/n)? ")
                if strInput.lower() == "y" or strInput.lower() == "yes":
                    SaveDataToFile()
                    #send program output   
                    print("Data was saved to file")
                else:
                    print("Not Saved!!!")
        else:
            break 
except Exception as e:
    print("Python Error message:" + str(e))

finally:
    print("End of Application!  Have a great day!")
