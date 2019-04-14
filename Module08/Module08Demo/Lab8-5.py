'''
Create a Customer Class that has a Customer Id, FirstName, and LastName
properties by inheriting code from your Person class.
'''

class Person(object):
    '''Base Class for Star Wars Characters'''

 # --Fields--
    # FirstName = None
    # LastName = None

 # --Constructor--
    def __init__(self,FirstName ="",LastName=""):
        # Attributes
        self.__FirstName = FirstName
        self.__LastName = LastName

        # use property
        self.FirstName = FirstName
        self.LastName = LastName


 # --Properties-- 
 # --First Name--
    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self,Value):
        self.__FirstName = Value

 # --Last Name--
    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self,Value):
        self.__LastName = Value

 # --Methods--
    def ToString(self):
        return "{} {}".format(self.FirstName,self.LastName)
    
    def __str__(self):
        return self.ToString()
 #--END--

# --Beginning of Customer Class--
class Customer(Person):
    '''Class Customer'''
    None
 # --Constructor--
    def __init__(self, ID, FirstName, LastName):
        # Attributes
        self.__ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        # super(Customer, self).__init__(FirstName, LastName)
    
 # --Attributes--
 # ID
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, Value):
        self.__ID = Value

 # --Methods--
    def ToString(self):
        '''Explicitly returns field data'''
        return "ID:{}, {} {}".format(str(self.__ID),self.FirstName,self.LastName)
    
    def __str__(self):
        '''Implicitly returns field data'''
        return self.ToString()
 # --END--


objE1 = Customer(1,"Han","Solo")
objE2 = Customer(2,"Princess Leia","Organa of Alderon")
print("\n*****STAR WARS CHARACTERS*****")
print(objE1.ToString())
print("\n----\o\-|o|-/o/----\n")
print(objE2)




