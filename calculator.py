import numpy as np

print("Welcome to the calculator!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: cannot divide by zero"
    else:
        return a / b
    
def sqrt(a):
    if a < 0:
        return "error: cannot take square root of negative number"
    elif a == 0:
        return "error: cannot take square root of zero"
    else:
        return np.sqrt(a)

def sqr(a):
    return a * a

def power(a, b):
    return a ** b

# Get input from the user
num1 = float(input("Enter first number: "))
op = input("enter operation: ")
num2 = None
if op != "sqrt" and op != "sqr":
    num2 = float(input("Enter second number: "))

if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
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
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
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
