#--- Make the class ---
class Person(object):
    FirstName = ""

    def ToString(self):
        return self.FirstName 
#End of class

# --- Use the class ----
# by making an object!
objP1 = Person()
objP1.FirstName = "Bob"

objP2 = Person()
objP2.FirstName = "Sue"

print(objP1.ToString())
print("-------------")
print(objP2.ToString())


fileName = input("Please enter file name: ")

objFile = open(fileName, +".txt")