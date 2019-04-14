#-------------------------------------#
    #Desc:  Holds Personal data
    #Dev:   RRoot 
    #Date:  12/12/2012
    #ChangeLog:(When,Who,What)
#-------------------------------------#

class Person(object):
    """ Base Class for Personal data """
    #--Fields--
    FirstName = ""
    LastName = ""
    #--Constructor--
        #Attributes
    #--Properties--   
    
    #--Methods--
    def ToString(self):
        return "{} {}".format(self.FirstName,self.LastName)
 
#--End of class--

# --- Use the class ----
# by making an object!
objP1 = Person()
objP1.FirstName = "Han"
objP1.LastName = "Solo"

objP2 = Person()
objP2.FirstName = "Pricess Leia"
objP2.LastName = "Orangana of Alderon"

print(objP1.ToString())
print("-------------")
print(objP2.ToString())
