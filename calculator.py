def operations_list():
    operations_list = ['+', '-', '*', '/']
    return operations_list

def get_number(prompt):
    while True:
        num_str = input(prompt)
        if num_str.isdigit() or (num_str.startswith("-") and num_str[1:].isdigit()):
            return float(num_str)
        print("Invalid input. Input must be positive or negative number.")

def get_opertion(prompt):
    while True:
        opertion_sign = input(prompt)
        if opertion_sign in operations_list():
            return opertion_sign
        print("Invalid input. Input must be sign from these list: ", operations_list())

def calculations(first_number, second_number, operation):
    if operation == "+":
        result = first_number + second_number
        return result
    if operation == "-":
        result = first_number - second_number
        return result
    if operation == "*":
        result = first_number * second_number
        return result
    if operation == "/":
        result = first_number / second_number
        return result