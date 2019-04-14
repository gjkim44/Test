"""
1)	Create a function that returns a list of the Sum, Difference, Product, and Quotient of two numbers.
2)	Display the results to the user.
3)	Divide you program into data, processing, and presentation sections.

"""

def total():
    A1 = int(input("please give a number  "))
    A2 = int(input("please give me a second number "))

    def math(num1,num2):
        add = float(num1 + num2)
        sub = float(num1 - num2)
        mult = float(num1 * num2)
        div = float(num1 / num2)

        # answer = ["sum = {}, dif = {}, prod = {}, quot = {}.".format(add,sub,mult,div)]

        answer = [add,sub,mult,div]
        return answer
        
    lstAnswer = math(A1,A2)
    print("For the values of",A1, "and",A2)
    print(
        """
        The sum is {},
        the Difference is {},
        The Product is {},
        The Quotient is {},
        """.format(lstAnswer[0],lstAnswer[1],lstAnswer[2],lstAnswer[3])
    )

total()