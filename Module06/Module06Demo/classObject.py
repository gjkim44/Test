# --- make the Class ---
class Customer(object):
    ID = None
    Name = None


    def ToString(self):
        return str(self.Id) + "," + str(self.Name)

# --- Use the Clasee ---

objCustomer1 = Customer() #This code creates a “Copy” of the class
objCustomer1.Id = 1
objCustomer1.Name = "Bob Smith"


objCustomer2 = Customer() #This code creates different “Copy”
objCustomer2.Id = 2
objCustomer2.Name = "Sue Jones"

print(objCustomer1.ToString())
print(objCustomer2.ToString())
