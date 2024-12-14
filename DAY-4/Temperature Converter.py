def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Conversion examples
c_temp = 25
f_temp = 77
print(f"{c_temp}°C in Fahrenheit:", celsius_to_fahrenheit(c_temp))
print(f"{f_temp}°F in Celsius:", fahrenheit_to_celsius(f_temp))
