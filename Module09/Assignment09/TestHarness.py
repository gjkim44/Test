if __name__ == "__main__":
    import Customers, DataProcessor, Persons
else:
    raise Exception("This file was not created to be imported ")

p1 = Persons.Person("Bob","Smith","50")
print(p1)

e1 = Customers.Customer(1, "Sue", "Jones", "49", "1111 Main St  Seattle, Wa 98103", "206 931 6127", "gk@gmail.com")
# print(e1)

Customers.CustomerList.AddCustomer(e1)
print(Customers.CustomerList.ToString())