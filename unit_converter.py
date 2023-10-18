def mass_units_SI(value, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000}
    result = value * SI[unit_in]/SI[unit_out]
    return result