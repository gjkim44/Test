#-------------------------------------#
#Desc:  Holds Personal data
#Dev:   RRoot 
#Date:  12/12/2012
#ChangeLog:(When,Who,What)
#-------------------------------------#

class Person(object):
    """ Base Class for Personal data """
  
    #--Fields--
    #FirstName = ""

    #--Constructor--
    def __init__(self, FirstName = ""):
        #Attributes
        self.__FirstName = FirstName
    
    #--Properties--
    #FirstName    
    @property  # (getter or accessor) 
    def FirstName(self):
        return self.__FirstName
    
    @FirstName.setter  # (setter or mutator)
    def FirstName(self, Value):
        self.__FirstName = Value 
 
    #--Methods--
    def ToString(self):
        return self.FirstName 
#--End of class--

# --- Use the class ----
# by making an object!
objP1 = Person("Bob")

objP2 = Person()
objP2.FirstName = "Sue" 

print(objP1.ToString())
print("-------------")
print(objP2.ToString())
