n1 = float(input("n1: "))
n2 = float(input("n2: "))

if n2 != 0:
    q1 = n1/n2
    print("the quotient of", n1, "by", n2, "is", q1)
else:
    print("Check for ZeroS")
try:
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
except:
    print("Check for zero")