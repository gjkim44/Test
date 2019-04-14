# Make a list
# To save it to a txt file
# it must be converted to a string
Id = str(1) 
Name = "Bob Smith"
lstRow1 = [Id, Name]
print(lstRow1)

# output to file
objFile = open("C:\_PythonClass\Module07\Module07Demo\Customers.txt", "a")
# objFile.writelines(lstRow1[0] + "," + lstRow1[1] + "\n")  
objFile.writelines("{},{}\n".format(lstRow1[0],lstRow1[1]))
objFile.close()

objFile = open("C:\_PythonClass\Module07\Module07Demo\Customers.txt", "r")
lstFileData = objFile.readlines()
objFile.close()
for row in lstFileData:
    print(row.strip())
print(lstFileData)
