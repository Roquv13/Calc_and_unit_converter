SI_mass = {'g':0.001, 'dag':0.01, 'kg':1.0, 't':1000}

def mass_units_dic(SI_mass):
    return SI_mass

def mass_units_keys():
    SI_keys = list(SI_mass.keys())
    return SI_keys

def mass_convert(value, unit_in, unit_out):
    SI = {'g':0.001, 'dag':0.01, 'kg':1.0, 't':1000}
    result = value * SI[unit_in]/SI[unit_out]
    return result