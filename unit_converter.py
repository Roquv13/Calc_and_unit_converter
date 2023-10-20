# Units SI dicionaries
SI_mass = {'g':0.001, 'dag':0.01, 'kg':1.0, 't':1000}
SI_len = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000}
SI_temp = ['C', 'F', 'K']

def print_units_list():
    print("Mass unit converter")
    print("It supports:", "\nMass: ", list(SI_mass.keys()), "\nLenght: ", list(SI_len.keys()), "\nTemperature: ", SI_temp)

def get_value(prompt):
    while True:
        value_str = input(prompt)
        if value_str.isdigit():
            return float(value_str)
        print("Invalid input. Input must be number.")

def get_unit(prompt):
    while True:
        opertion_sign = input(prompt)
        if opertion_sign in SI_mass or SI_len:
            return opertion_sign
        print("Invalid input. Input must be sign from these list: ", SI_mass, SI_len)

def convert(value, unit_in, unit_out):
    if unit_in in SI_mass:
        result = value * SI_mass[unit_in]/SI_mass[unit_out]
    elif unit_in in SI_len:
        result = value * SI_len[unit_in]/SI_len[unit_out]
    elif unit_in in SI_temp:
        if unit_in == "C":
            if unit_out == "K":
                result = value + 273.15
            elif unit_out == "F":
                result = value * 9/5 + 32
        elif unit_in == "K":
            if unit_out == "C":
                result = value - 273.15
            elif unit_out == "F":
                result = (value - 273.15) * 9/5 + 32
        elif unit_in == "F":
            if unit_out == "C":
                result = (value - 32) * 5/9
            elif unit_out == "K":
                result = (value - 32) * 5/9 + 273.15
    return result


def get_result():
    # User input
    value = get_value("Enter value to convert: ")
    unit_in = get_unit("Enter initial unit: ")
    unit_out = get_unit("Enter unit to convert to: ")

    # Display result
    result = convert(value, unit_in, unit_out)
    print("Result: ", result, unit_out)