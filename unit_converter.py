import unit_converter
def converter():
    
    '''
    The user can input a value to convert.
The user can select the units to convert from and to.
The user can view the converted value.
The user can convert between different units of measurement like length, weight, temperature, etc (more given below).
You can include the following units of measurement to convert between:

Length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
Weight: milligram, gram, kilogram, ounce, pound.
Temperature: Celsius, Fahrenheit, Kelvin. '''

    units_length = ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']
    units_weight = ['milligram', 'gram', 'kilogram', 'ounce', 'pound']
    units_temp = ['Celsius', 'Fahrenheit', 'Kelvin']
    
    category = input("Please select a category to convert from (length, weight, temperature): ").lower()
    if category == 'length':
        print("Available units for length conversion: ", units_length)
    elif category == 'weight':
        print("Available units for weight conversion: ", units_weight)
    elif category == 'temperature':
        print("Available units for temperature conversion: ", units_temp)
    else:
        print("Invalid category selected. Please try again.")
        return

    units_to_convert_from = []
    units_to_convert_to = []

    if category == 'length':
        units_to_convert_from = units_length
        units_to_convert_to = units_length
    elif category == 'weight':
        units_to_convert_from = units_weight
        units_to_convert_to = units_weight
    elif category == 'temperature':
        units_to_convert_from = units_temp
        units_to_convert_to = units_temp

    print("Available units for conversion: ", units_to_convert_from)

    from_unit = input("Please select a unit to convert from: ").lower()
    to_unit = input("Please select a unit to convert to: ").lower()

    if from_unit not in units_to_convert_from or to_unit not in units_to_convert_to:
        print("Invalid units selected. Please try again.")
        return

    
    value = float(input(f"Please enter the value in {from_unit}: "))
    converted_value = unit_converter.converter(value, from_unit, to_unit)
     
    
    print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")

converter()


