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

header("🧮 Number one.")

n1 = number_validator("✅ What's the first number?: ")

while True:
    header("🧮 Operations.")

    for item in operations:
        print(item)

    while True:
        pick = input("\n✅ Pick an operation: ").strip()
        if pick not in operations.keys():
            print(f"❌ '{pick}' is not a valid pick.\n")
        else:
            break

    header("🧮 Next Number.")
    n2 = number_validator("✅ What's the next number?: ", pick)
    result = round(operations[pick](n1, n2), 2)

    header('🧮 The result is...')
    print(f"✔ {n1} {pick} {n2} = {result}")

    while True:
        header('🧮 To continue?')
        choice = input(f"✔ 'y' to continue calculating with {result};\n✔ 'n' to start a new calculation;\n✔  or 'e' to exit.\n\n✅ Choice:  ").strip().lower()

        if choice == "y":
            os.system('cls')
            header("🧮 Let's calculate!")
            n1 = result
            print(f'The first number to calculate is {n1}')
            break
        elif choice == "n":
            os.system('cls')
            header("🧮 Let's calculate!")
            n1 = number_validator("✅ What's the first number?: ")
            break
        elif choice == 'e':
            header("👋🏾 Closing calculator...")
            sleep(1)
            sys.exit()
        else:
            os.system('cls')
            print(f"❌ '{choice}' is not a valid option.\n")
