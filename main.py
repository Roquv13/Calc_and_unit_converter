import calculator
import os
import unit_converter

def user_choice():
    while True:
        print("What do you want to do?")
        user_input = input("1. Calculate numbers\n2. Convert units\n3. Exit\n")
        if user_input == "":
            print("Field cannot be empty.")
        else:
            return int(user_input)

def next_action():
    action_continue = input("If you want to continue press ENTER")
    if not action_continue:
        os.system('cls' if os.name == 'nt' else 'clear')

user_input = user_choice()

while user_input == 1 or 2 or 3:
    if user_input == 1:
        print("Calculator supports these operations", calculator.operations_list())

        calculator.get_result()

        next_action()
        
    elif user_input == 2:
        unit_converter.print_units_list()
        
        unit_converter.get_result()

        next_action()
    
    elif user_input == 3:
        break
    
    user_input = user_choice()