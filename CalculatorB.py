import numpy as np

print("Welcome to the calculator!")

history = []
last_result = None  # stores the most recent numeric result for "ans"


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


def modulo(a, b):
    if b == 0:
        return "error: cannot modulo by zero"
    else:
        return a % b


def percentage(a, b):
    return (a / 100) * b


def log(a):
    if a <= 0:
        return "error: log undefined for zero or negative numbers"
    else:
        return np.log10(a)


SINGLE_ARG_OPS = ["sqrt", "sqr", "log"]
VALID_OPS = ["+", "-", "*", "/", "sqrt", "sqr", "power", "%", "percent", "log"]


def get_float(prompt):
    """Keep asking until the user enters a valid number.
    Typing 'ans' reuses the last numeric result, if one exists."""
    while True:
        value = input(prompt)
        if value.strip().lower() == "ans":
            if isinstance(last_result, (int, float)):
                print(f"Using ans = {last_result}")
                return float(last_result)
            else:
                print("No previous numeric result to use as ans")
                continue
        try:
            return float(value)
        except ValueError:
            print("Enter a valid number")


def get_operation(prompt):
    """Keep asking until the user enters a valid operation."""
    while True:
        op = input(prompt)
        if op in VALID_OPS:
            return op
        print("Enter a valid operation")


def do_calculation(num1, op, num2):
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
    elif op == "%":
        result = modulo(num1, num2)
    elif op == "percent":
        result = percentage(num1, num2)
    elif op == "log":
        result = log(num1)
    else:
        result = "Invalid operation"

    if num2 is not None:
        entry = f"{num1} {op} {num2} = {result}"
    else:
        entry = f"{op} {num1} = {result}"
    history.append(entry)

    return result


def show_history():
    if not history:
        print("No calculations yet.")
    else:
        print("\n--- Calculation History ---")
        for i, entry in enumerate(history, start=1):
            print(f"{i}. {entry}")
        print("----------------------------\n")


def clear_history():
    history.clear()
    print("History cleared.")


# Get input from the user
num1 = get_float("Enter first number (or 'ans'): ")
op = get_operation("choose operation (+, -, *, /, sqrt, sqr, power, %, percent, log): ")
num2 = None
if op not in SINGLE_ARG_OPS:
    num2 = get_float("Enter second number (or 'ans'): ")

result = do_calculation(num1, op, num2)
print("Result:", result)
if isinstance(result, (int, float)):
    last_result = result

recalculate = input("Do you want to perform another calculation? (yes/no/history/clear): ")
while recalculate.lower() in ("yes", "history", "clear"):
    if recalculate.lower() == "history":
        show_history()
    elif recalculate.lower() == "clear":
        clear_history()
    else:
        num1 = get_float("Enter first number (or 'ans'): ")
        op = get_operation("enter operation: ")
        num2 = None
        if op not in SINGLE_ARG_OPS:
            num2 = get_float("Enter second number (or 'ans'): ")

        result = do_calculation(num1, op, num2)
        print("Result:", result)
        if isinstance(result, (int, float)):
            last_result = result

    recalculate = input("Do you want to perform another calculation? (yes/no/history/clear): ")

if recalculate.lower() == "no":
    print("Thank you for using the calculator!")
else:
    print("Invalid input. Exiting the calculator.")