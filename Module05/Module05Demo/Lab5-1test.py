# 2)	Add code that lets users appends a new row of data.
# 3)	Add a loop that lets the user keep adding rows.
# 4)	Ask the user if they want to save the data to a file when they exit the loop.
# 5)	Save the data to a file if they say 'yes'


lstRow0 = ['Id','Name','Email']
lstRow1 = ['1','Bob Smith','BSmith@Hotmail.com']
lstRow2 = ['2','Sue Jones','SueJ@Yahoo.com']
lstRow3 = ['3','Joe James','JoeJames@Gmail.com']
lstTable =[lstRow0,lstRow1,lstRow2,lstRow3]
print(lstTable)

# 2)	Add code that lets users appends a new row of data.
#Make a New Row
while True:
    intId = int(input("Enter a ID: "))
    strName = input("Enter a Name: ")
    strEmail = input("enter a Email: ")
    lstNewRow = [intId,strName,strEmail]
    #Add to Table
    lstTable.append(lstNewRow)
    strAnswer = input("Add more data (y/n)")
    if strAnswer == 'n': break

print(lstTable)
strAnswer = input("Save Data to file (y/n)")
if strAnswer.lower() == "y":
    fileName = input("Please enter file name: ")

    objFile = open(fileName +".txt", "a")
    # objF = open("MyData.txt", "a")
    for lstRow in lstTable:
        objFile.write(str(lstRow)+ '\n')
    objFile.close()

