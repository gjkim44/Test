'''
1)	Make the FirstName and LastName attributes private in the constructor of your Person class
2)	Add a Accessors and Mutators property procedures for the FirstName and LastName attributes
'''

class StarWarsCharacters(object):
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
        return "{} {}".format(self.__FirstName,self.__LastName)

    def __str__(self):
        return self.ToString()

    
obj1 = StarWarsCharacters("Han","Solo")
obj2 = StarWarsCharacters("Princess Leia","Organa of Alderon")

print("\n*****STAR WARS CHARACTERS*****")
print(obj1.ToString())
print("\n----|o|-|o|-|o|----\n")
print(obj2.ToString())
print(obj1)
print(obj2)