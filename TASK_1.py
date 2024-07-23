def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    
    temp_value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    
    if unit == 'C':
        temp_fahrenheit = celsius_to_fahrenheit(temp_value)
        temp_kelvin = celsius_to_kelvin(temp_value)
        print(f"{temp_value}°C is equal to {temp_fahrenheit:.2f}°F and {temp_kelvin:.2f}K")
    
    elif unit == 'F':
        temp_celsius = fahrenheit_to_celsius(temp_value)
        temp_kelvin = fahrenheit_to_kelvin(temp_value)
        print(f"{temp_value}°F is equal to {temp_celsius:.2f}°C and {temp_kelvin:.2f}K")
    
    elif unit == 'K':
        temp_celsius = kelvin_to_celsius(temp_value)
        temp_fahrenheit = kelvin_to_fahrenheit(temp_value)
        print(f"{temp_value}K is equal to {temp_celsius:.2f}°C and {temp_fahrenheit:.2f}°F")
    
    else:
        print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

if __name__ == "__main__":
    main()
