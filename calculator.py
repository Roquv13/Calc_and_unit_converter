operations_list = ['+', '-', '*', '/']

def get_number(prompt):
    while True:
        num_str = input(prompt)
        if num_str.isdigit() or (num_str.startswith("-") and num_str[1:].isdigit()):
            return float(num_str)
        print("Invalid input. Input must be positive or negative number.")

def get_opertion(prompt):
    while True:
        opertion_sign = input(prompt)
        if opertion_sign.isalpha():
            return opertion_sign
        print("Invalid input. Input must be sign from these list: ", operations_list)
print("Calculator supports these operations", operations_list)

num1 = get_number("Enter first number for calculations: ")
num2 = get_number("Enter second number for calculations: ")
operation = input("Enter operations to do: ")

def calculations(first_number, second_number, operation_sign):
    if operation == "+":
        result = float(first_number) + float(second_number)
        return result

if operation in operations_list:
    result = calculations(num1, num2, operation)
    print(result)