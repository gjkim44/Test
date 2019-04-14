#------------Persons.py Module ---------------#
#Desc:  Classes that hold Personal data
#Dev:   RRoot 
#Date:  03/05/2019
#ChangeLog:(Who,When,What)
#  GKim, 3-06-19, Re-typed Persons module.  Added age to persons.
#---------------------------------------------#

if __name__ =="__main__":
    import datetime
    raise Exception("This file is not to be run on its own")

 # ---Person Class---
class Person(object):
    ''' Base Class for Personal Data '''

    # --Fields--
    __Counter = 0 # Developers, please use this as a private class field.

    # --Constructor--
    def __init__(self, FirstName = "", LastName = "", Age = ""):
        # --Attributes--
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Age = Age
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

    # Age
    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self, Value):
        self.__Age = Value

    # --Methods--
    def ToString(self):
        ''' Explicitly returns field data '''
        return "{}, {}, {}".format(str(self.__FirstName), str(self.__LastName), str(self.__Age))

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
