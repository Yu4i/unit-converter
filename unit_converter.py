def unit_converter():
    
    '''
    The user can input a value to convert.
The user can select the units to convert from and to.
The user can view the converted value.
The user can convert between different units of measurement like length, weight, temperature, etc (more given below).
You can include the following units of measurement to convert between:

Length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
Weight: milligram, gram, kilogram, ounce, pound.
Temperature: Celsius, Fahrenheit, Kelvin. '''

    units_lenght = ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']
    units_weight = ['milligram', 'gram', 'kilogram', 'ounce', 'pound']
    units_temp = ['Celsius', 'Fahrenheit', 'Kelvin']
    
    
    value_to_convert = float(input("Please Input a value to convert "))
    print("Please put in a proper value")


unit_converter()        
    
    
