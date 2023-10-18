def mass_units_dic():
    SI = {'g':0.001, 'dag':0.01, 'kg':1.0, 't':1000}
    return SI

def mass_units_keys():
    SI_keys = mass_units_dic
    return SI_keys

def mass_convert(value, unit_in, unit_out):
    SI = mass_units_dic
    result = value * SI[unit_in]/SI[unit_out]
    return result