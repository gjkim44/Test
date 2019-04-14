#------------Customer2.py ---------------#
#Desc:  Classes that hold employee data
#Dev:   RRoot 
#Date:  03/05/2019
#ChangeLog:(Who,When,What)
#  GKim, 3-6-19, Re-typed Employee module to Customer Module.  
# Added Id , Address, PhoneNumber, Email 
#  GKim, 3-08-19, Added Age and Age Verification function from Persons
#  GKim, 3-10-19, Created TFAge boolean variable to break out of loop in MyApp
#---------------------------------------------#

import datetime # imported datetime to calculate age
import Persons2
if __name__ == "__main__":
    raise Exception("This file is not meant to be run on its own!!")

 # ---Child Class---
class Customer(Persons2.Person):
    ''' Class for Customer data'''

 # ---Constructor---
    def __init__(self, Id = "", FirstName = "", LastName = "", Birthday = None, Address ="", PhoneNumber = "", Email = ""):
        # --Attributes--
        self.__Id = Id
        self.FirstName = FirstName
        self.LastName = LastName
        self.Birthday = Birthday
        self.__Address = Address
        self.__PhoneNumber = PhoneNumber
        self.__Email = Email

    # --Properties--
    # Id
    @property # getter
    def Id(self):
        return self.__Id

    @Id.setter # setter
    def Id(self, Value):
        self.__Id = Value

    # Address
    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, Value):
        self.__Address = Value

    #PhoneNumber
    @property
    def PhoneNumber(self):
        return self.__PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, Value):
        self.__PhoneNumber = Value 

    # Email
    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, Value):
        self.__Email = Value

    # --Methods--
    # Age Function
    def age(self):
        ''' Calculates age of customer'''
        today = datetime.date.today() # gets today date
        age = today.year - self.Birthday.year  # variable set to get customers age

        if today < datetime.date(today.year, self.Birthday.month, self.Birthday.day):
            # compares todays date to customers birth month and day, if within the same year
            age -= 1
        return age

    # Age Verification Function
    def ageVerification(self):
        VerAge = self.age() # variable to capture age from function age()
        TFAge = None # variable to return Boolean for if/else condition in loop on MyApp
        if int(VerAge) <= 17: # compares age to input from user on Customer
           TFAge = False # Returns False if customer is 17yrs or younger
           print("Person is not old enough to be our customer!")
           return TFAge  # returning boolean result
        
        
    

    def ToString(self):
        '''Explicitly returns field data'''
        return "{}, {}, {}, {}, {}, {}, {}".format(str(self.Id), self.FirstName, self.LastName, str(self.Birthday),self.Address,
                                        self.PhoneNumber, self.Email)

    def __str__(self):
        '''Implicity returns field data'''
        return self.ToString()
 # --End of Class Customer--

class CustomerList(object):
    ''' Static class for holding the Customer Data '''

    __lstCustomers = []

    # --Methods--
    @staticmethod
    def AddCustomer(Customer):
        if str(Customer.__class__) == "<class 'Customers2.Customer'>":
            CustomerList.__lstCustomers.append(Customer)
        else:
            raise Exception("Only Customer objects can be added to this list")
    
    @staticmethod
    def ToString():
        strData = "Id,FirstName,LastName,Age,Address,PhoneNumber,Email\n"
        for item in CustomerList.__lstCustomers:
            strData += "{}, {}, {}, {}, {}, {}, {}\n".format(str(item.Id), item.FirstName, item.LastName, str(item.Birthday),item.Address,
                                    item.PhoneNumber, item.Email)
        return strData

    @staticmethod
    def __str__():
        strData = CustomerList.ToString
        return strData

 # --End of Class
