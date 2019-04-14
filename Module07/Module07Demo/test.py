


# #-- Data --
# strData = None # Holds returned data
# objFile = None # Handle for a text file

# #--- create data classes ---
# class Customer(object):
#     Id = None
#     Name = None

#     def ToString(self):
#         return str(self.Id) + "," + str(self.Name)
# #End of class

# # --- Use the class  ----
# # Create an object
# objCustomer1 = Customer()

# # Write data to the object's fields
# objCustomer1.Id = input("Enter an Id: ") 
# objCustomer1.Name = input("Enter a Name: ")

# # Read data from the object's fields
# strData = objCustomer1.ToString()

# # Use the data
# # output to file
# objFile = open("C:\_PythonClass\Module07\Module07Demo\Customers.txt", "a")
# objFile.write(strData + "\n")
# objFile.close()

# # read from the file
# objFile = open("C:\_PythonClass\Module07\Module07Demo\Customers.txt", "r")
# print(objFile.read())
# objFile.close()


import pickle

example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.dat","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.dat","rb")
example_dict = pickle.load(pickle_in)


print(example_dict)
print(example_dict)
