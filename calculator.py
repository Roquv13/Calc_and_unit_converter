def operations_list():
    operations_list = ['+', '-', '*', '/', '^', 'root', 'mod']
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
        while second_number == 0:
            print("You cannot divide by zero.")
            second_number = get_number("Enter second number for calculations:")
        result = first_number / second_number
        return result
    if operation == "^":
        result = first_number ** second_number
        return result
    if operation == "root":
        result = first_number ** (1/second_number)
        if result % 1 > 0:
            return int(result) + 1
        else:
            return int(result)
    if operation == "mod":
        result = first_number % second_number
        return result

def get_result():
    operation = get_opertion("Enter operations to do: ")

    if operation in operations_list():
        if operation == "^":
            num1 = get_number("Enter number to be exponentiated: ")
            num2 = get_number("Enter degree of exponentiation: ")
        elif operation == "root":
            num1 = get_number("Enter number to calculate root: ")
            num2 = get_number("Enter degree of root: ")
        else:
            num1 = get_number("Enter first number for calculations: ")
            num2 = get_number("Enter second number for calculations: ")
        
        result = calculations(num1, num2, operation)
        return print("Result of calculations: ", result)