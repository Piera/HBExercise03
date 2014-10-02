
from arithmetic2 import add, subtract, multiply, divide, square, cube, power, mod

while True:#repeat forever unless unser enters 'q':
    try:
    #    read input
        calculation=raw_input("Enter your calculation; example format + 2 1; or press 'q' to quit. ")
    #    tokenize input
        token=calculation.split(" ")
    #   if the first token is 'q', quit
        if token[0] == "q":
            break
        else:
    #   call the appropriate math function
            if token[0] == "+":
                print(add(int(token[1]), int(token[2])))

            elif token[0] == "-":
                print(subtract(int(token[1]), int(token[2])))

            elif token[0] == "*":
                print(multiply(int(token[1]), int(token[2])))

            elif token[0] == "/":
                print divide(float(token[1]), float(token[2]))

            elif token[0] == "square":
                print(square(int(token[1])))

            elif token[0] == "cube":
                print(cube(int(token[1])))

            elif token[0] == "pow":
                print(power(int(token[1]), int(token[2])))

            elif token[0] == "mod":
                print(mod(int(token[1]), int(token[2])))

            else:
                print("I don't understand!")
                
    except ValueError:
        print("Please enter numbers! Or 'q' to quit!")
        continue