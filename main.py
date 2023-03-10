import sys
import os
from functions import number_validator, add, subtract, multiply, divide, header
from logo import logo
from time import sleep

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

print(logo)

header("š§® Number one.")

n1 = number_validator("ā What's the first number?: ")

while True:
    header("š§® Operations.")

    for item in operations:
        print(item)

    while True:
        pick = input("\nā Pick an operation: ").strip()
        if pick not in operations.keys():
            print(f"ā '{pick}' is not a valid pick.\n")
        else:
            break

    header("š§® Next Number.")
    n2 = number_validator("ā What's the next number?: ", pick)
    result = round(operations[pick](n1, n2), 2)

    header('š§® The result is...')
    print(f"ā {n1} {pick} {n2} = {result}")

    while True:
        header('š§® To continue?')
        choice = input(f"ā 'y' to continue calculating with {result};\nā 'n' to start a new calculation;\nā  or 'e' to exit.\n\nā Choice:  ").strip().lower()

        if choice == "y":
            os.system('cls')
            header("š§® Let's calculate!")
            n1 = result
            print(f'The first number to calculate is {n1}')
            break
        elif choice == "n":
            os.system('cls')
            header("š§® Let's calculate!")
            n1 = number_validator("ā What's the first number?: ")
            break
        elif choice == 'e':
            header("šš¾ Closing calculator...")
            sleep(1)
            sys.exit()
        else:
            os.system('cls')
            print(f"ā '{choice}' is not a valid option.\n")
