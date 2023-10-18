import unit_converter
import calculator

#Mass converter
print("Mass unit converter")
unit_available = unit_converter.mass_units_keys()
print("It supports: ", unit_available)
value = float(input("Enter value to convert: "))
unit_in = input("Enter initial unit: ")
unit_out = input("Enter unit to convert to: ")
result = unit_converter.mass_convert(value, unit_in, unit_out)
print(result)