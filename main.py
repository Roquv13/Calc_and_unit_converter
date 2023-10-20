import calculator
import os
import unit_converter

def user_choice():
    print("What do you want to do?")
    user_input = int(input("1. Calculate numbers\n2. Convert units\n3. Exit\n"))
    return user_input

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
        unit_converter.units_list()
        
        # User input
        value = unit_converter.get_value("Enter value to convert: ")
        unit_in = unit_converter.get_unit("Enter initial unit: ")
        unit_out = unit_converter.get_unit("Enter unit to convert to: ")

        # Display result
        result = unit_converter.convert(value, unit_in, unit_out)
        print("Result: ", result, unit_out)

        next_action()
    
    elif user_input == 3:
        break
    
    user_input = user_choice()