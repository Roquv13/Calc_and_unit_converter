import calculator
import os
def user_choice():
    print("What do you want to do?")
    user_input = int(input("1. Calculate numbers\n2. Convert units\n3. Exit\n"))
    return user_input

user_input = user_choice()

while user_input == 1 or 2 or 3:
    if user_input == 1:
        print("Calculator supports these operations", calculator.operations_list())

        num1 = calculator.get_number("Enter first number for calculations: ")
        num2 = calculator.get_number("Enter second number for calculations: ")
        operation = calculator.get_opertion("Enter operations to do: ")

        if operation in calculator.operations_list():
            result = calculator.calculations(num1, num2, operation)
            print("Result of calculations: ", result)


        next_action = input("If you want to continue press ENTER")
        if not next_action:
            os.system('cls' if os.name == 'nt' else 'clear')
        
    elif user_input == 2:
        print("2")
    elif user_input == 3:
        break
    
    user_input = user_choice()