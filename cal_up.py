def calculator():
    print("insert values to calculate")

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

    print(y)
    print(len(y))

    result = y[0]
    i = 1
    while i < len(y):
        op = y[i]
        next_num = y[i + 1]
        if op == "+":
            result = result + next_num
        elif op == "-":
            result = result - next_num
        elif op == "*":
            result = result * next_num
        elif op == "/":
            if next_num == 0:
                result = "cannot divide by zero"
                break
            result = result / next_num
        i += 2
    print(result)
    calculator()

calculator()
