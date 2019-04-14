# Create a function that prints the Sum, Difference, Product, and Quotient of two numbers.

def math(num1,num2):
    add = float(num1 + num2)
    sub = float(num1 - num2)
    mult = float(num1 * num2)
    div = float(num1 / num2)

    answer = ("sum = {}, dif = {}, prod = {}, quot = {}.".format(add,sub,mult,div))
    return answer 

print(math(10,2))