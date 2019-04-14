#--- data code ---
v1 = 10
v2 = 5
decAnswer = None

#--- processing code ---
class MathFunctions(object):
    # Define the function
    @staticmethod
    def AddValues(value1, value2):
        return value1 + value2

        


# --- presentation (I/O) code ---

decAnswer = MathFunctions.AddValues(v1, v2)
print("The Sum of the values"
    + str(v1) + "and" + str(v2) + "is:" + str(decAnswer)) 