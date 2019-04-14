'''
1)	Create a constructor for your Person class
2)	Add FirstName and LastName attributes to the constructor of your Person class

'''

class StarWarsCharacters(object):
    '''Base Class for Star Wars Characters'''

# --Fields--
#     FirstName = ""
#     LastName = ""

# --Constructor--
    def __init__(self,FirstName = "",LastName= ""):
        #attributes
        self.FirstName = FirstName
        self.LastName = LastName

    def ToString(self):
        return "{} {}".format(self.FirstName,self.LastName)

obj1 = StarWarsCharacters("Han","Solo")
# obj1.FirstName = "Han"
# obj1.LastName = "Solo"

obj2 = StarWarsCharacters("Princess Leia","Organa of Alderon")
# obj2.FirstName = "Princess Leia"
# obj2.LastName = "Organa of Alderon"

print("\n*****STAR WARS CHARACTERS*****")
print(obj1.ToString())
print("\n----|o|-|o|-|o|----\n")
print(obj2.ToString())
