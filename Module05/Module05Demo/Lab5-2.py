# 2)	Add code that lets users appends a new row of data.
# 3)	Add a loop that lets the user keep adding rows.
# 4)	Ask the user if they want to save the data to a file when they exit the loop.
# 5)	Save the data to a file if they say 'yes'



dictRow1 = {'Id': 1 ,'Name':'Bob Smith','Email':'BSmith@Hotmail.com'}
dictRow2 = {'Id': 2,'Name':'Sue Jones','Email':'SueJ@Yahoo.com'}
dictRow3 = {'Id': 3,'Name':'Joe James','Email':'JoeJames@Gmail.com'}
lstTable =[dictRow1,dictRow2,dictRow3]
print(lstTable)

# 2)	Add code that lets users appends a new row of data.
#Make a New Row
while True:
    intId = int(input("Enter a ID: "))
    strName = input("Enter a Name: ")
    strEmail = input("enter a Email: ")
    dictNewRow = {"ID": intId,"Name": strName,"Email":strEmail}
    #Add to Table
    lstTable.append(dictNewRow)
    strAnswer = input("Add more data (y/n)")
    if strAnswer.lower() == 'n': break

print(lstTable)
strAnswer = input("Save Data to file (y/n)")
if strAnswer.lower() == "y":
    objF = open("MyData.txt", "a")
    for dictRow in lstTable:
        objF.write(str(dictRow)+ '\n')
    objF.close()

