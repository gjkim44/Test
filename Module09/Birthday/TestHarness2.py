if __name__ == "__main__":
    import Customers2, DataProcessor2, Persons2, datetime
else:
    raise Exception("This file was not created to be imported ")

p1 = Persons2.Person("Bob","Smith","50")
print(p1)

e1 = Customers2.Customer(1, "Sue", "Jones", datetime.date(2009, 11, 29), "1111 Main St  Seattle, Wa 98103", "206 931 6127", "gk@gmail.com")
print(e1)
print(e1.ageVerification())

Customers2.CustomerList.AddCustomer(e1)
print(Customers2.CustomerList.ToString())
print(e1.ageVerification())