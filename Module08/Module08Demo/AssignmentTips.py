# 2)	Add code that lets users appends a new row of data.
# 3)	Add a loop that lets the user keep adding rows.
# 4)	Ask the user if they want to save the data to a file when they exit the loop.
# 5)	Save the data to a file if they say 'yes'

class Person(object):
    # --Fields--
    # strName = ""

    # --Constructor--
    def __init__(self, Name): # lets users appends a new row of data to a collection
        # Attribute
        self.__Name = Name
        
 # --Properties--
 # Name
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Value):
        self.__Name = Value

 # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return str(self.__Name)
    
    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
 # --END--

class Customer(Person):
    # --Fields--
    # intID = 0
    # strEmail = ""

    # --Constructor--
    def __init__(self, ID, Name, Email): # lets users appends a new row of data to a collection
        # Attributes
        self.__ID = ID
        super(Customer, self).__init__(Name)
        self.__Email = Email

 # --Properties--
 # ID
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, Value):
        self.__ID = Value

# Email
    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, Value):
        self.__Email = Value

 # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return "{}, {}, {}".format(str(self.ID),str(self.Name),str(self.Email))
    
    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
 # --END--    

class CustomerSaver(object):

    def SaveCustomerDataFile(self): #
        None

objC1 = Customer(1,'Bob Smith','BSmith@Hotmail.com')
objC2 = Customer(2,'Sue Jones','SueJ@Yahoo.com')
objC3 = Customer(3,'Joe James','JoeJames@Gmail.com')
lstTable =[objC1,objC2,objC3]
# print(lstTable)

# 2)	Add code that lets users appends a new row of data.
#Make a New Row
while True:
    intID = int(input("Enter a ID: "))
    strName = input("Enter a Name: ")
    strEmail = input("enter a Email: ")
    objC = Customer(intID,strName,strEmail)
    # dictNewRow = {"ID": intId,"Name": strName,"Email":strEmail}
    #Add to Table
    lstTable.append(objC)
    strAnswer = input("Add more data (y/n)")
    if strAnswer.lower() == 'n': 
        break

# print(lstTable)
strAnswer = input("Save Data to file (y/n)")
if strAnswer.lower() == "y":
    objF = open("Assignmet08Data.txt", "a")
    strAllText = ""
    for item in lstTable:
        strData = item.ToString() + '\n\r'
        objF.write(strData)
        strAllText += strData
    objF.close()
    print("The following data was saved to a file: \n\r",strAllText)
else:
    print("Data was not saved!")

