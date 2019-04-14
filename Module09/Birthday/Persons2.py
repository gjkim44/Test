#------------Persons.py Module ---------------#
#Desc:  Classes that hold Personal data
#Dev:   RRoot 
#Date:  03/05/2019
#ChangeLog:(Who,When,What)
#  GKim, 3-06-19, Re-typed Persons module. Added Birthday to persons, changing it from Age.
#  GKim, 3-07-19, Created Age function, and Age Verification function.
#  GKim, 3-08-19, Moved Age Function, and Age Verification function to Customers
#---------------------------------------------#


if __name__ =="__main__":
    raise Exception("This file is not to be run on its own")

 # ---Person Class---
class Person(object):
    ''' Base Class for Personal Data '''

    # --Fields--
    __Counter = 0 # Developers, please use this as a private class field.

    # --Constructor--
    def __init__(self, FirstName = "", LastName = "", Birthday = None):
        # --Attributes--
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Birthday = Birthday
        Person.__SetObjectCount() # Private Method

    # --Properties--
    # FirstName
    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, Value):
        self.__FirstName = Value

    # LastName
    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, Value):
        self.__LastName = Value

    # Birthday
    @property
    def Birthday(self):
        return self.__Birthday

    @Birthday.setter
    def Birthday(self, Value):
        self.__Birthday = Value

    # --Methods--
    

    def ToString(self):
        ''' Explicitly returns field data '''
        return "{}, {}, {}".format(str(self.__FirstName), str(self.__LastName), str(self.__Birthday))

    def __str__(self):
        ''' Implicitly returns field data'''
        return self.ToString()

    @staticmethod
    def GetObjectCount():
        return Person.__Counter

    @staticmethod
    def __SetObjectCount():
        Person.__Counter += 1

 # -End of class Person--
