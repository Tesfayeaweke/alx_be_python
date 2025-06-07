# Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# conversion functions
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


while True:
    temp = input("Enter the temperature to convert: ")
    try:
        temp = float(temp)
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

while True:

    if unit == "c":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        break
    elif unit == "f":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        break
    else:
        print("Error,enter either C or F!")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()









