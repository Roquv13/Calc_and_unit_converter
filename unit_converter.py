SI_mass = {'g':0.001, 'dag':0.01, 'kg':1.0, 't':1000}
SI_len = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}

#Define convert function
def convert(value, unit_in, unit_out):
    if unit_in in SI_mass:
        default_unit = SI_mass
    elif unit_in in SI_len:
        default_unit = SI_len
    result = value * default_unit[unit_in]/default_unit[unit_out]
    return result

# Mass converter
print("Mass unit converter")
print("It supports:", "\nMass: ", list(SI_mass.keys()), "\nLenght: ", list(SI_len.keys()))

# User input
value = float(input("Enter value to convert: "))
unit_in = input("Enter initial unit: ")
unit_out = input("Enter unit to convert to: ")

# Display result
result = convert(value, unit_in, unit_out)
print("Result: ", result, unit_out)