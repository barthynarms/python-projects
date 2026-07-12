import numpy as np

def calculator():
    print("insert values to calculate\n# = square root\n$ for = square\n^ = power\n+ = addition\n- = subtraction\n* = multiplication\n/ = division"
          )

    x = input()
    xseperated = ""
    y = []

    for j in x:
        if j.isdigit() or j == ".":
            xseperated += j
        else:
            if xseperated != "":
                y.append(float(xseperated))
                xseperated = ""
            y.append(j)

    if xseperated != "":
        y.append(float(xseperated))

    # print(y)
    # print(len(y))

    result = y[0]
    i = 1
    while i < len(y):
        op = y[i]
        if op == "#":
            if result <= 0:
                result = "error: cannot take square root of negative number"
                break
            result = np.sqrt(result)
            i += 1
        elif op == "$":
            result = result * result
            i += 1
        # elif op == "!":
            #CONTINUE FROM HERE TO INTEGRATE FACTORIAL CALCULATIONS AND FIBONACCI CALCULATIONS
        else:
            next_num = y[i + 1]
            if op == "+":
                result = result + next_num
            elif op == "-":
                result = result - next_num
            elif op == "*":
                result = result * next_num
            elif op == "^":
                result = result ** next_num
            elif op == "/":
                if next_num == 0:
                    result = "cannot divide by zero"
                    break
                result = result / next_num
            i += 2
    print(result, "\n")
    recalculate = input("Do you want to perform another calculation? (yes/no): ")
    while recalculate.lower() == "yes":
        calculator()
        if recalculate.lower() == "no":
            print("Thank you for using the calculator!")
    else:
        if recalculate.lower() != "no" and recalculate.lower() != "yes":
            print("Invalid input. Exiting the calculator.")
calculator()