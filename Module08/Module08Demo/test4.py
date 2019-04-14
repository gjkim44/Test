class Person(object):
    """ Base Class for Personal data """
    #-------------------------------------#
    #Desc:  Holds Personal data
    #Dev:   RRoot 
    #Date:  12/12/2012
    #ChangeLog:(When,Who,What)
    #-------------------------------------#
    
    #--Fields--
    #FirstName = ""
    __Counter = 0 # Hey Devs, please consider this a private field!

    #--Constructor--
    def __init__(self, FirstName = ""):
        #Attributes
        self.__FirstName = FirstName
        Person.__Counter += 1 # You do not use the self keyword    
  
#--Properties--
       
    #FirstName    
    @property #getter(accessor) 
    def FirstName(self):
        return self.__FirstName
    
    @FirstName.setter #(mutator)
    def FirstName(self, Value):
        self.__FirstName = Value
        
    
    #--Methods--
    def ToString(self):
        """Explictly returns field data"""
        return self.FirstName
    
    def __str__(self):
        """Implictly returns field data"""        
        return self.FirstName
    
    @staticmethod
    def GetObjectCount(): # You do not need the self keyword
        return Person.__Counter
 
# --- Use the class ----
objP1 = Person("Bob")
print(Person.GetObjectCount())

objP2 = Person()
objP2.FirstName = "Sue" 
print(Person.GetObjectCount())

print(objP1)
print("-------------")
print(objP2)

print(Person.__Counter) 
