# No setup
#repeat forever:
while True:
#    read input
    calculation=raw_input("Enter something!")
#    tokenize input
    token=calculation.split(" ")
    print token
#   if the first token is 'q', quit
    if token[0] == "q":
        break
    else:
#   call the appropriate math function
    if token[0] == "+":
        add(token[1],token[2])

    elif token[0] == "-":
        subtract(token[1], token[2])

    elif token[0] == "*":
        multiply(token[1], token[2])

    elif token[0] == "/":
        divide(token[1], token[2])




def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 ** 2

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2