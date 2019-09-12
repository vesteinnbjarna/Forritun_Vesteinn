
def celsius_to_farenheit(celsius_float):
    """ Convert Celsius to Fahrenheit. """
    return celsius_float * 1.8 + 32

print("Convert Celsius to Fahrenheit.")
celsius_float = float(input('Enter degrees in celsius:'))

fahrenheit_float = celsius_to_farenheit (celsius_float)

print(celsius_float," converts to ", fahrenheit_float," Fahrenheit")
