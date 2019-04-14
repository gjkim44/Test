# 1.	Create a script that uses a two-dimensional tuple to hold the following data:
# Id	Name	Email
# 1	Bob Smith	BSmith@Hotmail.com
# 2	Sue Jones	SueJ@Yahoo.com
# 3	Joe James	JoeJames@Gmail.com


header =("ID","Name","Email")

info =(
    ("1","Bob Smith","BSmith@hotmail.com"),
    ("2","Sue Jones", "SueJ@Yahoo.com"),
    ("3","Joe James", "JoeJames@Gmail.com"),
)


for item in header:
    print(item)

for item in info:
    print("-" * 30)
    for x in item:
        print(x)