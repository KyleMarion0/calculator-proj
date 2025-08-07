import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    num1 = int(input("Enter the first number: "))

    while True:
        for symbol in calc_dict:
            print(symbol)
        calc_op = input("Enter an operator: ")
        num2 = int(input("Enter the second number: "))

        result = calc_dict[calc_op](num1, num2)
        print(f"{num1} {calc_op} {num2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if cont == "y":
            num1 = result
        else:
            break

calculator()
