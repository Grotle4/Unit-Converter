#script for running all the converts for measurements depending on webpage


def calc_length(unit, unit_from, unit_to):
    print(type(unit))
    to_meters = {
                "millimeter": 0.001,
                "centimeter": 0.01,
                "meter": 1.0,
                "kilometer": 1000.0,
                "inch": 0.0254,
                "foot": 0.3048,
                "yard": 0.9144,
                "mile": 1609.344
                }
    
    meters = int(unit) * to_meters[unit_from]
    converted = meters / to_meters[unit_to]
    rounded_converted = round(converted, 4)

    return rounded_converted

    
def calc_weight(unit, unit_from, unit_to):
    to_kilograms = {
        "milligram": 0.000001,     
        "gram": 0.001,          
        "kilogram": 1.0,        
        "ounce": 0.0283495231,
        "pound": 0.45359237     
    }

    kilograms = int(unit) * to_kilograms[unit_from]
    converted = kilograms / to_kilograms[unit_to]

    rounded_converted = round(converted, 4)

    return rounded_converted

def calc_temp(unit, unit_from, unit_to):
    if unit_from == "celsius":
        celsius = int(unit)
    elif unit_from == "fahrenheit":
        celsius = (int(unit) - 32) * 5/9
    elif unit_from == "kelvin":
        celsius = int(unit) - 273.15

    # Step 2: Convert from Celsius → target
    if unit_to == "celsius":
        converted = celsius
    elif unit_to == "fahrenheit":
        converted = (celsius * 9/5) + 32
    elif unit_to == "kelvin":
        converted = celsius + 273.15

    rounded_converted = round(converted, 4)

    return rounded_converted

def conversion(unit, unit_from, unit_to, type):
    match type:
        case "length":
            converted = calc_length(unit, unit_from, unit_to)
            return converted
        case "weight":
            converted = calc_weight(unit, unit_from, unit_to)
            return converted
        case "temperature":
            converted = calc_temp(unit, unit_from, unit_to)
            return converted