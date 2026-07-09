import numpy as np

print("Welcome to the calculator!")

def add(a, b, c):
    return a + b + c

def subtract(a, b, c):
    return a - b - c

def multiply(a, b, c):
    return a * b * c

def divide(a, b):
    if a == 0:
        return "expression undefine"
    else:
        return b / a
    
def sqrt(a):
    if a <= 0:
        return "error: cannot take negative number and zero sqrt"
    else:
        return np.sqrt(a)

def sqr(a):
    return a * a

def power(a, b):
    return a ** b

# Get input from the user
num1 = float(input("Enter first number: "))
op = input("choose operation (+, -, *, /, sqrt, sqr, power): ")
num2 = None
if op != "sqrt" and op != "sqr":
    num2 = float(input("Enter second number: "))
    op = input("choose operation (+, -, *, /, power): ")   
elif op != "power" and op != "divide":
    num3 = float(input("enter third number: "))

if op == "+":
    result = add(num1, num2, num3)
elif op == "-":
    result = subtract(num1, num2, num3)
elif op == "*":
    result = multiply(num1, num2, num3)
elif op == "/":
    result = divide(num1, num2)
elif op == "sqrt":
    result = sqrt(num1)
elif op == "sqr":
    result = sqr(num1)
elif op == "power":
    result = power(num1, num2)
else:
    result = "Invalid operation"

print("Result:", result)

recalculate = input("Do you want to perform another calculation? (yes/no): ")
while recalculate.lower() == "yes":
    num1 = float(input("Enter first number: "))
    op = input("enter operation: ")
    num2 = None
    if op != "sqrt" and op != "sqr":
        num2 = float(input("Enter second number: "))

    if op == "+":
        result = add(num1, num2, num3)
    elif op == "-":
        result = subtract(num1, num2, num3)
    elif op == "*":
        result = multiply(num1, num2, num3)
    elif op == "/":
        result = divide(num1, num2)
    elif op == "sqrt":
        result = sqrt(num1)
    elif op == "sqr":
        result = sqr(num1)
    elif op == "power":
        result = power(num1, num2)
    else:
        result = "Invalid operation"

    print("Result:", result)
    recalculate = input("Do you want to perform another calculation? (yes/no): ")
    if recalculate.lower() != "yes":
        print("Thank you for using the calculator!")
    else:
        if recalculate.lower() != "no" and recalculate.lower() != "yes":
            print("Invalid input. Exiting the calculator.")

