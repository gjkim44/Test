# Get the argument value
import sys
strData = sys.argv[1]
print(strData)

# Execute if 1, 2, or 3 is selected
if strData == "1":
    print("You chose one")
elif strData == "2":
    print("You chose two")
elif strData == "3":
    print("You chose three")
else:
    print("Please chose 1,2, or 3")
# Print "You chose one" only if option 1 is selected.
# Print "You chose two" execute only if option 2 is selected.
# Print "You chose three" execute only if option 3 is selected.
# Print "Please choose 1, 2, or 3"
