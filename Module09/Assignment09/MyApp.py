#-------------------------------------------------#
# Title: CustomerApp
# Dev:   RRoot
# Date:  03/05/2019
# Desc: This application mges Customer data
# CheLog: (Who, When, What)
#  GKim, 3-06-19, Re-typed MyApp and changed to customer.  Added age condition to 
# print message and break out of loop 
#
#-------------------------------------------------#
if __name__ == "__main__":
    import DataProcessor, Customers
else:
    raise Exception("This file wasn't created to be imported")

#-- Data --# 
# Variable constants
objCust = None # Customer objCust
intId = 0 # CustomerId
gIntLastId = 0 # Records the last CustomerId used in the client
strFirstName = "" # Customer's First name
strLastName = "" # Customer's Last name
intAge = "" # Customer's Age
strAddress = "" # Customer's Address
strPhoneNumber = "" # Customer's Phone Number
strEmail = "" # Customer's Email
strInput = "" #temporary user input

# -- Processing --#
# perform tasks
def ProcessNewCustomerData(Id, FirstName, LastName, Age, Address, PhoneNumber, Email):
    try:
        # Create Customer objCust
        objCust = Customers.Customer()
        objCust.Id = Id
        objCust.FirstName = FirstName
        objCust.LastName = LastName
        objCust.Age = Age
        objCust.Address = Address
        objCust.PhoneNumber = PhoneNumber
        objCust.Email = Email
        Customers.CustomerList.AddCustomer(objCust)
    except Exception as e:
        print(e)

def SaveDataToFile():
    try:
        objF = DataProcessor.File()
        # objF.FileName = "C:\_PythonClass\Module09\Assignment09\CustomerData.txt"
        objF.FileName = "CustomerData.txt"
        objF.TextData = Customers.CustomerList.ToString()
        print("Data was saved here, Congrats!!")
        objF.SaveData()
    except Exception as e:
        print(e)

# -- Presentation (I/O) --#
# __main__
        
# User input
strUserInput = ""
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
        # Customer Age from user
        intAge = int(input("Enter Customer Age: "))
        if intAge <= 17:
            print("The Customer must be 18yrs to added!")
            break
        # else:
        #     continue
        # Customer Address from User
        print("\nCustomer Address ex: 1111 Main St. Seattle, WA 98108")
        strAddress = input("Enter Customer Address: ")
        # Customer Phone Number 
        print("\nCustomer Phone Number ex: 555 555 5555")
        strPhoneNumber = input("Enter Customer Phone Number: ")
        # Customer Email
        print("\nCustomer Email ex: JaneDoe@hotmail.com")
        strEmail = input("Enter Customer Email: ")
        
        #Process input
        ProcessNewCustomerData(intId, strFirstName, strLastName, intAge, strAddress, strPhoneNumber, strEmail)
    else:
        break 

#send program output
print("Here is the Current Data: ")
print("------------------------")
print(Customers.CustomerList.ToString())

#user input
strInput = input("Would you like to save this data to file(y/n)? ")
if strInput.lower() == "y" or strInput.lower() == "yes":
    SaveDataToFile()
    #send program output   
    print("Data was saved to file")
else:
    print("Not Saved!!!")

print("End of Application!  Have a great day!")
