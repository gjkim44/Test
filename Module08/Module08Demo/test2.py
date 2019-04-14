#-------------------------------------#
#Desc:  Holds Personal data
#Dev:   RRoot 
#Date:  12/12/2012
#ChangeLog:(When,Who,What)
#-------------------------------------#

#--- Make the class ---
class Person(object):
    """ Base Class for Personal data """

    #--Fields--
    FirstName = None
    LastName = None
    #--Constructor--
    def __init__(self, FirstName,LastName):
        #Attributes
        self.FirstName = FirstName
        self.LastName = LastName
    
    #--Properties--   
    
    #--Methods--
    def ToString(self):
        return "{} {}".format(self.FirstName,self.LastName) 

#--End of class--

# --- Use the class ----
# by making an object!
objP1 = Person("Han","Solo")
#objP1.FirstName = "Bob"

objP2 = Person("Princess Leia","Organa of Alderon")
#objP2.FirstName = "Sue"

print("*****STAR WARS CHARACTERS*****")
print(objP1.ToString())
print("|o|-|o|-|o|")
print(objP2.ToString())
