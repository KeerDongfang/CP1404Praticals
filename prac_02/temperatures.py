def main():
    temperature_in_celsius = float(input("Please enter the temperature in Celsius: "))
    convert_the_temperatures(temperature_in_celsius)


def convert_the_temperatures(temperature_in_celsius):
    """convert the temperature from Celsius to Fahrenheit"""
    temperature_in_fahrenheit = temperature_in_celsius * 9 / 5 + 32
    print(f"Result: {temperature_in_fahrenheit:.2f} F")


main()
